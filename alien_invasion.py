import sys
from time import sleep

import pygame

import settings
import ship
import bullet
from alien import Alien
from game_stat import GameState
from button import Button
from scoreboard import Scoreboard


class AllienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game and create game resources."""
        pygame.init()

        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Allien Invasion")
        self.stats = GameState(self)
        self.button = Button(self, "Play game")
        self.ship = ship.Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.scoreboard = Scoreboard(self)

    def _check_fleet_edges(self):
        """Respond if any alien meets the edge of the screen."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_alien(self, alien_number, row_number):
        """Create an alien."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # Spacing between each alien is equal to one alien width.
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x // (alien_width * 2)
        # Determine the number of rows
        available_height_y = self.settings.screen_height - \
            3 * alien_height - self.ship.rect.height
        number_alliens_rows = available_height_y // (alien_height * 2)

        # Create the fleet of aliens.
        for row_number in range(number_alliens_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _fire_bullet(self):
        """Create a new bullet and add it to the group of bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = bullet.Bullet(self)
            self.bullets.add(new_bullet)

    def _check_play_button(self, mouse_pos):
        """Start a game if button Play is pressed."""
        button_clicked = self.button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            pygame.mouse.set_visible(False)
            self.stats.reset_stat()
            self.stats.game_active = True
            self.scoreboard.prep_score()

            # Delete all remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

    def _check_keydown_events(self, event):
        """Respond to key keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_events(self):
        """Respond to keypress and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_bullet_alien_collision(self):
        """Check for any bullet that have hit aliens. If so delete this bullet and the alien."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_score * len(aliens)
                self.scoreboard.check_high_score()
            self.scoreboard.prep_score()

        if not self.aliens:
            # Destroy existing bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                return True

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement left ships
            self.stats.ships_left -= 1

            # Delete all remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_bullets(self):
        """Update position of bullets"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update position of all aliens."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collision or aliens hitting the bottom of the screen
        if pygame.sprite.spritecollideany(self.ship, self.aliens) or self._check_aliens_bottom():
            self._ship_hit()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets:
            bullet.draw()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.scoreboard.show_score()

        if not self.stats.game_active:
            self.button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run_game(self):
        """Start main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()


if __name__ == '__main__':
    game = AllienInvasion()
    game.run_game()
