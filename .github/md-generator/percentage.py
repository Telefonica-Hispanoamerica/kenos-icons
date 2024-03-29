import os

def count_files(path):
    return len(os.listdir(path))


icons_default_light = count_files(r'/Users/yayo/Kactus/mistica-icons/icons/default/1.Light')
icons_default_regular = count_files(r'/Users/yayo/Kactus/mistica-icons/icons/default/2.Regular')
icons_default_filled = count_files(r'/Users/yayo/Kactus/mistica-icons/icons/default/3.Filled')
total_default = icons_default_light + icons_default_regular + icons_default_filled

icons_o2_light = count_files(r'/Users/yayo/Kactus/mistica-icons/icons/o2/1.Light')
icons_o2_regular = count_files(r'/Users/yayo/Kactus/mistica-icons/icons/o2/2.Regular')
icons_o2_filled = count_files(r'/Users/yayo/Kactus/mistica-icons/icons/o2/3.Filled')
total_o2 = icons_o2_light + icons_o2_regular + icons_o2_filled

# print(int(total_default))
# print(int(total_o2))
# print(icons_o2)

default_percent = 100
o2_percent = (int((total_o2 * 100) / total_default))
# blau_percent = (int((total_blau * 100) / total_default))

default_bar = ("Default set  " + (int(default_percent / 10) * 2) * "█" + "░" * (
            abs(int(default_percent / 10) - 10) * 2) + "  " + str(int(default_percent))
      + "%")
o2_bar = ("O2 set       " + (int(o2_percent / 10) * 2) * "█" + "░" * (abs(int(o2_percent / 10) - 10) * 2) + "  " + str(
    int(o2_percent))
      + "%")

print(default_bar)
print(o2_bar)



