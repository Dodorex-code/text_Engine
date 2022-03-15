from operator import index
import winsound

class core():
    def render_simple_text(name, text):
        inp_4 = input("=>")
        if name != "desc":
            print(name + ": " + text)
        else:
            print(text)
    
    def render_multi_text(name, texts=[]):
        for text in texts:
            if name != "desc":
                print(name + ": " + text)
            else:
                print(text)
            texts.remove(text)
        if len(texts) > 0:
            inp_1 = input("=>")
            core.render_multi_text(name, texts)
    
class goal_system():
    goal_achieved = False
    goal_description = "no goal"
    def give_goal(giver_name, text):
        #inp_2 = input("=>")
        core.render_simple_text(giver_name, text)
    def complete_goal(text):
        #inp_3 = input("=>")
        core.render_simple_text("desc", text)
        goal_system.goal_achieved = True

class dialog():
    def main_text(npc_name, initial_text, option1, option2, option3, dialog1, dialog2, dialog3):
        core.render_simple_text(npc_name, initial_text)
        core.render_simple_text("1", option1)
        core.render_simple_text("2", option2)
        core.render_simple_text("3", option3)
        selected_option = input("[enter 1, 2 or 3] =>")
        if selected_option == "1":
            core.render_simple_text(npc_name, dialog1)
            return(1)
        elif selected_option == "2":
            core.render_simple_text(npc_name, dialog2)
            return(2)
        elif selected_option == "3":
            core.render_simple_text(npc_name, dialog3)
            return(3)

class art():
    def art_loader(row1, row2, row3, row4, row5, row6,row7, row8, row9, row10, row11, row12):
        print(row1)
        print(row2)
        print(row3)
        print(row4)
        print(row5)
        print(row6)
        print(row7)
        print(row8)
        print(row9)
        print(row10)
        print(row11)
        print(row12)

    def intro_render(row1, row2, row3, row4, row5, row6):
        print(row1)
        print(row2)
        print(row3)
        print(row4)
        print(row5)
        print(row6)

class settings():

    class text_fg:
        BLACK   = '\033[30m'
        RED     = '\033[31m'
        GREEN   = '\033[32m'
        YELLOW  = '\033[33m'
        BLUE    = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN    = '\033[36m'
        WHITE   = '\033[37m'
        RESET   = '\033[39m'

    class text_bg:
        BLACK   = '\033[40m'
        RED     = '\033[41m'
        GREEN   = '\033[42m'
        YELLOW  = '\033[43m'
        BLUE    = '\033[44m'
        MAGENTA = '\033[45m'
        CYAN    = '\033[46m'
        WHITE   = '\033[47m'
        RESET   = '\033[49m'

    class text_style:
        BRIGHT    = '\033[1m'
        DIM       = '\033[2m'
        NORMAL    = '\033[22m'
        RESET_ALL = '\033[0m'

    text_color = text_fg.RESET
    background_color = text_fg.RESET
    fg_text_style = text_style.RESET_ALL

    def set_text_color_black():
        settings.text_color = settings.text_fg.BLACK
        print(settings.text_color)
    
    def set_text_color_red():
        settings.text_color = settings.text_fg.RED
        print(settings.text_color)

    def set_text_color_green():
        settings.text_color = settings.text_fg.GREEN
        print(settings.text_color)

    def set_text_color_yellow():
        settings.text_color = settings.text_fg.YELLOW
        print(settings.text_color)

    def set_text_color_blue():
        settings.text_color = settings.text_fg.BLUE
        print(settings.text_color)

    def set_text_color_magenta():
        settings.text_color = settings.text_fg.MAGENTA
        print(settings.text_color)

    def set_text_color_cyan():
        settings.text_color = settings.text_fg.CYAN
        print(settings.text_color)

    def set_text_color_white():
        settings.text_color = settings.text_fg.WHITE
        print(settings.text_color)

    def set_text_color_reset():
        settings.text_color = settings.text_fg.RESET
        print(settings.text_color)

    def set_background_color_black():
        settings.background_color = settings.text_bg.BLACK
        print(settings.background_color)

    def set_background_color_red():
        settings.background_color = settings.text_bg.RED
        print(settings.background_color)

    def set_background_color_greeen():
        settings.background_color = settings.text_bg.GREEN
        print(settings.background_color)

    def set_background_color_yellow():
        settings.background_color = settings.text_bg.YELLOW
        print(settings.background_color)
    
    def set_background_color_blue():
        settings.background_color = settings.text_bg.BLUE
        print(settings.background_color)

    def set_background_color_magenta():
        settings.background_color = settings.text_bg.MAGENTA
        print(settings.background_color)

    def set_background_color_cyan():
        settings.background_color = settings.text_bg.CYAN
        print(settings.background_color)

    def set_background_color_white():
        settings.background_color = settings.text_bg.WHITE
        print(settings.background_color)

    def set_background_color_reset():
        settings.background_color = settings.text_bg.RESET
        print(settings.background_color)

    def set_text_style_brigth():
        settings.fg_text_style = settings.text_style.BRIGHT
        print(settings.fg_text_style)

    def set_text_style_dim():
        settings.fg_text_style = settings.text_style.DIM
        print(settings.fg_text_style)

    def set_text_style_normal():
        settings.fg_text_style = settings.text_style.NORMAL
        print(settings.fg_text_style)

    def set_text_style_reset():
        settings.fg_text_style = settings.text_style.RESET_ALL
        print(settings.fg_text_style)

class audio():
    def play_sound(filename):
        winsound.PlaySound(filename, winsound.SND_FILENAME)

    def play_beep_spund(beep_frequency, beep_duration):
        winsound.Beep(beep_frequency,beep_duration)

class path():
    def add_path(paths=[]):
        last_path_index = len(paths)
        path_num = 0
        for choice in paths:
            current_index = paths.index(choice, 0, last_path_index)
            if current_index == 0:
                pass
            else:
                path_num += 1
            print(str(path_num) + ": " + choice)
        inp_5 = int(input("=>"))
        if inp_5 <= last_path_index and  inp_5 >= 0:
            return(paths[inp_5])