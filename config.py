import colors

screen_width = 800
screen_height = 600
background_image = 'images/bg.jpg'

frame_rate = 120

row_count = 6
brick_width = 60
brick_height = 20
brick_color = colors.INDIANRED4
offset_y = brick_height + 10

ball_speed = 10
ball_radius = 10
ball_color = colors.DARKGOLDENROD1

paddle_width = 80
paddle_height = 20
paddle_color = colors.ALICEBLUE
paddle_speed = 6

status_offset_y = 5

text_color = colors.YELLOW1
initial_lives = 3
lives_right_offset = 85
lives_offset = screen_width - lives_right_offset
score_offset = 5

font_name = 'Courier New'
font_size = 17

effect_duration = 20

sounds_effects = dict(
    brick_hit='sound_effects/brick_hit.wav',
    effect_done='sound_effects/effect_done.wav',
    paddle_hit='sound_effects/paddle_hit.wav',
    level_complete='sound_effects/level_complete.wav',
)

message_duration = 3

button_text_color = colors.WHITE,
button_normal_back_color = colors.INDIANRED1
button_hover_back_color = colors.INDIANRED2
button_pressed_back_color = colors.INDIANRED3

menu_offset_x = 20
menu_offset_y = 300
menu_button_w = 80
menu_button_h = 50
