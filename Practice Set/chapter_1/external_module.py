#3. Install an external module and use it to perform an operation of your interest.

#pip install emoji(command to use emoji module)

# PS C:\Users\ranej\OneDrive\Desktop\Practice_Python> pip install emoji
# Collecting emoji
#   Downloading emoji-2.15.0-py3-none-any.whl.metadata (5.7 kB)
# Downloading emoji-2.15.0-py3-none-any.whl (608 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 608.4/608.4 kB 5.6 MB/s  0:00:00
# Installing collected packages: emoji
# Successfully installed emoji-2.15.0

import emoji

print(emoji.emojize("python is fun :snake: :rocket:"))

print(emoji.emojize("I love coffee :pink_heart:"))


"""
| Emoji | Name                                |
| ----- | ----------------------------------- |
| 😀    | `:grinning_face:`                   |
| 😃    | `:grinning_face_with_big_eyes:`     |
| 😄    | `:grinning_face_with_smiling_eyes:` |
| 😊    | `:smiling_face_with_smiling_eyes:`  |
| 😎    | `:smiling_face_with_sunglasses:`    |
| 😂    | `:face_with_tears_of_joy:`          |
| 😢    | `:crying_face:`                     |
| 😍    | `:smiling_face_with_heart-eyes:`    |
| 😘    | `:face_blowing_a_kiss:`             |
| 😡    | `:enraged_face:`                    |
| ❤️    | `:red_heart:`                       |
| 💙    | `:blue_heart:`                      |
| 💚    | `:green_heart:`                     |
| 💛    | `:yellow_heart:`                    |
| 👍    | `:thumbs_up:`                       |
| 👎    | `:thumbs_down:`                     |
| 👏    | `:clapping_hands:`                  |
| 🙏    | `:folded_hands:`                    |
| 💪    | `:flexed_biceps:`                   |
| 👋    | `:waving_hand:`                     |
| 🎉    | `:party_popper:`                    |
| 🎂    | `:birthday_cake:`                   |
| 🎁    | `:wrapped_gift:`                    |
| ⭐     | `:star:`                            |
| 🌟    | `:glowing_star:`                    |
| 🔥    | `:fire:`                            |
| 🌈    | `:rainbow:`                         |
| ☀️    | `:sun:`                             |
| 🌙    | `:crescent_moon:`                   |
| 🌍    | `:globe_showing_Europe-Africa:`     |
| 🐍    | `:snake:`                           |
| 🐶    | `:dog_face:`                        |
| 🐱    | `:cat_face:`                        |
| 🦁    | `:lion:`                            |
| 🐼    | `:panda:`                           |
| 🍎    | `:red_apple:`                       |
| 🍕    | `:pizza:`                           |
| 🍔    | `:hamburger:`                       |
| ☕     | `:hot_beverage:`                    |
| 🍩    | `:doughnut:`                        |
| 🚗    | `:automobile:`                      |
| 🚀    | `:rocket:`                          |
| ✈️    | `:airplane:`                        |
| 🚲    | `:bicycle:`                         |
| 💻    | `:laptop:`                          |
| 📱    | `:mobile_phone:`                    |
| 📚    | `:books:`                           |
| ✏️    | `:pencil:`                          |
| 🏆    | `:trophy:`                          |
| ⚽     | `:soccer_ball:`                     |
| 🎵    | `:musical_note:`                    |
| 🎮    | `:video_game:`                      |

"""