# 1) Import required modules:
#    a) Import `math` to calculate distance for collision detection.
#    b) Import `random` to generate random enemy positions.
#    c) Import `pygame` to create the game window, load images, and handle events.

# 2) Create constants to control game settings:
#    a) Screen size, player start position, enemy start range.
#    b) Enemy movement speed (X and Y), bullet speed, collision distance threshold.

# 3) Initialize pygame using `pygame.init()`.

# 4) Create the game window (screen) using `pygame.display.set_mode(...)`.

# 5) Load background image using `pygame.image.load('background.png')`.

# 6) Set the game title and icon:
#    a) Use `pygame.display.set_caption("Space Invader")`.
#    b) Load icon image `ufo.png` and apply using `pygame.display.set_icon(icon)`.

# 7) Setup the player:
#    a) Load the player image `player.png`.
#    b) Set initial player position using `playerX` and `playerY`.
#    c) Create `playerX_change = 0` to control horizontal movement.

# 8) Setup enemies using lists (multiple enemies):
#    a) Create empty lists for enemy image, x/y positions, and x/y movement changes.
#    b) Set `num_of_enemies = 6`.

# 9) Use a loop to create each enemy:
#    a) Load enemy image `enemy.png` and append it to `enemyImg`.
#    b) Set random starting X position within the screen width.
#    c) Set random starting Y position between ENEMY_START_Y_MIN and ENEMY_START_Y_MAX.
#    d) Set initial X speed (ENEMY_SPEED_X) and Y drop speed (ENEMY_SPEED_Y).

# 10) Setup bullet:
#     a) Load bullet image `bullet.png`.
#     b) Set bullet starting positions and movement speed.
#     c) Use `bullet_state = "ready"` to track if bullet can be fired or is already moving.

# 11) Setup score display:
#     a) Initialize `score_value = 0`.
#     b) Load a font using `pygame.font.Font(...)`.
#     c) Set score text position (textX, textY).

# 12) Setup game-over text font using a larger font size.

# 13) Define helper functions:
#     a) `show_score(x, y)` to render and display the score on the screen.
#     b) `game_over_text()` to display "GAME OVER" on the screen.
#     c) `player(x, y)` to draw the player image at (x, y).
#     d) `enemy(x, y, i)` to draw the i-th enemy at (x, y).
#     e) `fire_bullet(x, y)`:
#        - Set `bullet_state` to "fire"
#        - Draw the bullet slightly offset from the player position.
#     f) `isCollision(enemyX, enemyY, bulletX, bulletY)`:
#        - Calculate distance between enemy and bullet using the distance formula.
#        - Return True if distance is less than COLLISION_DISTANCE.

# 14) Start the main game loop with `running = True`.

# 15) Every frame inside the loop:
#     a) Clear the screen and draw the background image.

# 16) Handle events (keyboard and quit):
#     a) If `pygame.QUIT`, stop the loop.
#     b) If a key is pressed (`pygame.KEYDOWN`):
#        - LEFT arrow sets `playerX_change = -5`.
#        - RIGHT arrow sets `playerX_change = 5`.
#        - SPACE fires the bullet only if `bullet_state` is "ready":
#          i) Set `bulletX = playerX`
#          ii) Call `fire_bullet(bulletX, bulletY)`
#     c) If key is released (`pygame.KEYUP`) for LEFT/RIGHT:
#        - Set `playerX_change = 0` to stop movement.

# 17) Update player movement:
#     a) Add `playerX_change` to `playerX`.
#     b) Clamp player position so it stays inside the screen boundaries.

# 18) Update enemy movement for each enemy:
#     a) If any enemy goes below Y > 340:
#        - Move all enemies off-screen (enemyY = 2000)
#        - Display "GAME OVER"
#        - Break out of enemy loop.
#     b) Move enemy horizontally using `enemyX_change[i]`.
#     c) If enemy hits left/right edge:
#        - Reverse direction by multiplying speed by -1.
#        - Move enemy downward by adding `enemyY_change[i]`.
#     d) Check collision between the enemy and bullet:
#        - If collision occurs:
#          i) Reset bullet position and set bullet_state back to "ready".
#          ii) Increase score by 1.
#          iii) Respawn enemy at a new random position.
#     e) Draw the enemy on the screen.

# 19) Update bullet movement:
#     a) If bullet goes off the top of the screen (`bulletY <= 0`):
#        - Reset bulletY and set `bullet_state = "ready"`.
#     b) If bullet_state is "fire":
#        - Draw the bullet.
#        - Move the bullet upward by decreasing `bulletY`.

# 20) Draw the player, show the score, and update the display:
#     a) Draw player at (playerX, playerY).
#     b) Display score using `show_score(textX, textY)`.
#     c) Refresh the screen using `pygame.display.update()`.