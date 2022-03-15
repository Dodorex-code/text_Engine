from engine import *
import example_game_art
health = 74
gold = 0
#INTRO
r1 = "===================="
r2 = "=       ||         ="
r3 = "=     //  //       ="
r4 = "=     >-<>-<       ="
r5 = "=       ==         ="
r6 = "===================="
art.intro_render(r1,r2,r3,r4,r5,r6)
player_name = input("Enter your name: ")
audio.play_sound("Example_Intro_Sound")

core.render_simple_text("Merlin", "Hey, could get me 3 red flowers. I will restore your health as a reward.")
art.art_loader(example_game_art.merlin1,example_game_art.merlin2,example_game_art.merlin3,example_game_art.merlin4,example_game_art.merlin5,example_game_art.merlin6,example_game_art.merlin7,example_game_art.merlin8,example_game_art.merlin9,example_game_art.merlin10,example_game_art.merlin11,example_game_art.merlin12)
goal_system.give_goal("Merlin", "Bring the dragon Merlin 3 red flowers.")
core.render_multi_text(player_name, texts=["Where youd I find such flowes.", "I will look over there.", "hmmm... maybe I should look behind that old tree.", "Ah yes, finally. 3 red flowers."])
goal_system.complete_goal("You brought the flowers to Merlin and he restored your health")
health = 100
audio.play_beep_spund(440,200)
audio.play_beep_spund(540,180)
audio.play_beep_spund(640,160)
core.render_simple_text("desc", "You now have " + str(health) + " health.")
core.render_simple_text(player_name, "you walk for a while until you see a man hiding behind a bush.")
art.art_loader(example_game_art.caldron1,example_game_art.caldron2,example_game_art.caldron3,example_game_art.caldron4,example_game_art.caldron5,example_game_art.caldron6,example_game_art.caldron7,example_game_art.caldron8,example_game_art.caldron9,example_game_art.caldron10,example_game_art.caldron11,example_game_art.caldron12)
dialog1 = dialog.main_text("Caldron", "Hey,  you! Be quiet!", "Why?", "Who are you?", "Get out of my way!", "Beause you will wake up the forest troll over there!", "I am Caldron, a Warrior from the little city of baldren.", "Fuck you!")
if dialog1 == 1:
    goal_system.give_goal("Caldron", "Go and kill that troll and I will reward you with 10 gold.")
    core.render_simple_text("desc", "You sneak behind the troll.")
    core.render_simple_text("desc", "Slowly , step by step you get closer...")
    core.render_simple_text("desc", "AND THEN YOU GRAB HIM BY HIS NECK AND CHOKE HIM TO DEATH!")
    core.render_simple_text("desc", "Caldron comes running towards you")
    core.render_simple_text("desc", "He seems verry happy and gives you 10 gold")
    gold += 10
    core.render_simple_text("desc", "you now have " + str(gold) + " gold.")
else:
    core.render_simple_text("desc", "You quickly walk away.")
    core.render_simple_text("caldron", "Hey, wait! I have to tell you something.")
    path1 = path.add_path(paths=["Wait and see what he has to say", "yell at him for annoying you.", "run even faster"])
    if path1 == "Wait and see what he has to say":
        core.render_simple_text("Caldron", "I wanted to ask you if you would like to help me with a problem I have at home.")
        core.render_simple_text(player_name, "Sorry ,but I have to go now.")
    elif path1 == "yell at him for annoying you.":
        core.render_simple_text(player_name, "Dont annoy me with your dumb questions, loser.")
        core.render_simple_text("desc", "he looks at you with fury in his eyes. Caldron proceeds to draw his sword and chop your head off.")
    elif path1 == "run even faster":
        core.render_simple_text("desc", "you start running as fast as you can. he doesent even try to chase you.")
    else:
        print(path1)
        core.render_simple_text("desc", "You are confused and leave.")