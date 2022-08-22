import os
from subprocess import call
import time
import sys
from datetime import datetime
import argparse
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.sql import SqlLexer
from colorama import init, Fore, Back, Style
from rich.console import Console
from rich.progress import track
from rich.table import Table
import threading
from queue import Queue
import shutil


init(autoreset=True)

console = Console()

################################################################################################################
minecraft_srv_autocomplete = WordCompleter([
    'back', 'exit', 'options', 'help', 'set', 'ping', 'REGION', 'PORT', 'run', 'get', 'host'], ignore_case=True)

tcp_auto = WordCompleter([
 'back', 'exit', 'options', 'help', 'set', 'REGION', 'PORT', 'run'], ignore_case=True)

http_complete = WordCompleter([
    'back', 'exit', 'options', 'help', 'set', 'REGION', 'PORT', 'run'], ignore_case=True)

Authtoken_complete = WordCompleter([
    'token', 'exit', 'help', 'back'], ignore_case=True)

help_autocomplete = WordCompleter([
    'exit', 'help', 'back'], ignore_case=True)

ssh_autocomplete = WordCompleter([ 'exit', 'help' ],ignore_case=True)

################################################################################################################

class Minecraft:
    def __init__(self):
        self.options = { # available options to be set by user
            "REGION": "",
            "PORT": ""
        }
    def minefractSRV(self):
        session = PromptSession(
            lexer=PygmentsLexer(SqlLexer), completer=minecraft_srv_autocomplete)
        while True:
            try:
                mc_input = session.prompt('AUTONGROK(GAME-HOSTING)~# ')
                parsed_mc_input = mc_input.split() # split the input into seperate items in a list for easier access
                command = parsed_mc_input[0].lower() # setting the first item of parsed input (most likeley "set") to a seperate variable
                # checking the executed command
                if command == "set": # if set is used
                    variable = parsed_mc_input[1].upper() # set the variable chosen (Either RHOST or PORT) to the "variable" variable
                    value = " ".join(parsed_mc_input[2:]) # set the value you specified to the "value" varaible
                    if variable in self.options: # validation that the value exits
                        print(f"{variable} -> {value}") # outputting the variable and value set to it
                        self.options[variable] = value # actually setting the value specified to the variable name specified (LHOST or LPORT)
            except KeyboardInterrupt:
                continue
            
            except IndexError:
                return self.minefractSRV()


            if mc_input == 'options':
                output_cleaner_uwu = "\n".join((f"{option} -> {value}" for option, value in self.options.items())) # output all possible options that can be set with the "set" command
                print(output_cleaner_uwu)
            
            elif mc_input == "run":
                file_path = os.path.realpath(__file__)
                chdir_uwu = file_path[:85]
                os.chdir(chdir_uwu)
                port_optiom = self.options["PORT"]
                region_option = self.options["REGION"]
                os.system(f".\\ngrok.exe --region {region_option} tcp {port_optiom}")
                
            elif mc_input == "Get Host":
                os.system(f"ping o.tcp.ngrok.io") # its going to auto ping ngrok 0.tco.ngrok.io if yoiu have the correct setup (making sure that it is 0.tcp.ngrok.io)   


            elif mc_input == 'help':
                table = Table(title="Making A Minecraft Server (JAVA)")
                table.add_column("TYPE", justify="right", style="Green", no_wrap=True)
                table.add_column("Instruction", style="Red")
                table.add_column("Notes", style="Magenta" )

                table.add_row("Step 0", "I highly suggest you make another terminal as you'll need it for later steps.")
                table.add_row("Step 1", "Create a Single Player Minecraft World.")
                table.add_row("Step 2", "After Getting or if you're already in, hit escape to go to the quick menue.", "Litterally hit the Esc button on your keyboard")
                table.add_row("Step 3", "Click the button that says, ""Open to LAN"" this will open you to a menue. Click Next to Continue", "The menue mentioned will change the gamerules of the world, so enabling cheats will grant OP to the players joining.")
                table.add_row("Step 4", "With this Port, copy the port, and paste it into the 'port' area in this script", "Use, 'set port', to do so. And make sure to specify region using, 'set region'.")
                table.add_row("Step 5", "After confirming these two using the options quck menue in the script type run.", "To better explain, typing 'options' will let you see the inputed port and region.")
                table.add_row("Step 6", "After typing 'run' the tunnel will open. With opening the tunnel a menue will pop up. If the URL in the 'Forwarding' section has a zero, restart until it does. Once it does do not kill it for the remainder of this process.", " ""For example: tcp://4.tcp.ngrok.io:16275"" the forwarding will look like this but since there's a 4 in there we need to restart until it's a 0. And when I mean 'restart' I mean hit Ctrl+C and type 'Run' again to make the scrip do it again.")
                table.add_row("Step 7", "Once you have the URL in a zero format, copy from the zero to the o. With this you'll ping it.", " For example: It will look like this '0.tcp.ngrok.io', after copying, use either the ping in the script or type 'ping' with the corresponding URL you're pinging in another terminal. For Example: 'ping 0.tcp.ngrok.io'.") # you only use f strings if you are going to print a function or call another variable within a statement for examples os.system(f"cd C:\\{your_directory}")
                table.add_row("Step 8", "After pinging you'll get the IP address, copy the address in the 'Ping statistics for' and give it your friend with the ending numbers from earlier.", "For example: '1.111.11.111' is the IP and the ending numbers from ealier (I'll take it from the previous URL: 16275) and so it'll end up like this; 1.111.11.111:16275.")
                table.add_row("Step 9", "With those numbers have your friend enter those numbers into the 'Direct Connection' input in multiplayer, and like that you can play Minecraft with your friend.", "If it's not obvious enough, that button on the bottom of the screen that says 'Direct Connection', after clicking that it'll open a black bar. Click the black bar under 'Server Address', paste what you did the entire process for. And click the 'join server' button. Depending on your connection, it might take a bit.")
                
                console = Console()
                console.print(table)

            elif command.lower() == 'back':
                main()

            elif command.lower() == 'exit':
                print(Style.BRIGHT + Fore.RED + 'Peace homie')
                sys.exit()
            
            return self.minefractSRV()

class tcppanel:
    
    def __init__(self):
        self.options = { # available options to be set by user
            "PORT": "",
            "REGION": ""
        }


    def tcpmain(self):
        
        session = PromptSession(
            lexer=PygmentsLexer(SqlLexer), completer=tcp_auto)

        while True:
            try:
                tcp_input = session.prompt('TCP~# ')
                parsed_tcp_input = tcp_input.split() # split the input into seperate items in a list for easier access
                command = parsed_tcp_input[0].lower() # setting the first item of parsed input (most likeley "set") to a seperate variable
                # checking the executed command

                if command == "set": # if set is used
                    variable = parsed_tcp_input[1].upper() # set the variable chosen (Either RHOST or PORT) to the "variable" variable
                    value = " ".join(parsed_tcp_input[2:]) # set the value you specified to the "value" varaible
                    if variable in self.options: # validation that the value exits
                        print(f"{variable} -> {value}") # outputting the variable and value set to it
                        self.options[variable] = value # actually setting the value specified to the variable name specified (LHOST or LPORT)

                elif tcp_input == 'options':
                    output_cleaner_uwu = "\n".join((f"{option} -> {value}" for option, value in self.options.items())) # output all possible options that can be set with the "set" command
                    print(output_cleaner_uwu)
                
                elif tcp_input == "run":
                    fuck = self.options["PORT"]
                    shit = self.options["REGION"]
                    other = shit.lower()
                    os.system(f".\\ngrok.exe --region {other} tcp {fuck}")

                elif tcp_input == "help":
                    table = Table(title="Making a TCP Tunnel")
                    table.add_column("TYPE", justify="right", style="Green", no_wrap=True)
                    table.add_column("Instruction", style="Red")

                    table.add_row("Simple Explanation", "TCP Tunneling is the act of, using a two way connection between your client IP and a SSH server to smuggle a protocal that calls to another IP that's blocked via firewall from your direct client but not the SSH server.")
                    table.add_row("Step 1", "Input Region using 'set region', and then add your region on the script.") # you only use f strings if you are going to print a function or call another variable within a statement for examples os.system(f"cd C:\\{your_directory}")
                    table.add_row("Step 2", "Input the port of the server using the 'set port' command in the script.")
                    table.add_row("Step 3", "Check the region and port using the 'options' command to make sure ngrok works.")
                    table.add_row("Step 4", "Use the command 'run' to have ngrok run the command.")
                    
                    console = Console()
                    console.print(table)

                elif command.lower() == 'exit':
                    print(Style.BRIGHT + Fore.RED + 'Peace homie')
                    exit()
        
                elif command.lower() == 'back':
                    main()

            except KeyboardInterrupt:
                continue
            except IndexError:
                return self.tcpmain()

            return self.tcpmain()

class SmallHttpPeen:
    def __init__(self):
        self.options = { # available options to be set by user
            "PORT": "",
            "REGION": ""
        }


    def HTTPpannel(self):
        
        session = PromptSession(
            lexer=PygmentsLexer(SqlLexer), completer=http_complete)
        
        while True:
            try:
                httppannel_input = session.prompt('HTTP~# ')
                parsed_http_input = httppannel_input.split() # split the input into seperate items in a list for easier access
                command = parsed_http_input[0].lower() # setting the first item of parsed input (most likeley "set") to a seperate variable
                # checking the executed command

                if command == "set": # if set is used
                    variable = parsed_http_input[1].upper() # set the variable chosen (Either RHOST or PORT) to the "variable" variable
                    value = " ".join(parsed_http_input[2:]) # set the value you specified to the "value" varaible
                    if variable in self.options: # validation that the value exits
                        print(f"{variable} -> {value}") # outputting the variable and value set to it
                        self.options[variable] = value # actually setting the value specified to the variable name specified (LHOST or LPORT)

                elif httppannel_input == 'options':
                    output_cleaner_uwu = "\n".join((f"{option} -> {value}" for option, value in self.options.items())) # output all possible options that can be set with the "set" command
                    print(output_cleaner_uwu)
                
                elif httppannel_input == 'help':
                    print("If you haven't seen the TCP help section, we are doing the same there exept there's some veriation.")
                    table = Table(title="HTTP Help")
                    table.add_column("STEPS", justify="right", style="Green", no_wrap=True)
                    table.add_column("EXPLANATION", style="Red")
                    table.add_column("NOTE", style="cyan")

                    table.add_row("Step 1", "Set port of the server you're connecting to.", "Use the 'set' command in the script to set the port or region for the later step.")
                    table.add_row("Step 2", "Set your region.", "If you leave this blank it'll default to US.")
                    table.add_row("Step 3", "Check the options using the 'options' command in the script.")
                    table.add_row("Step 4", "After checking use the 'run' command to launch the http tunnel.")
                    table.add_row("Step 5", "ping the address or check by opening the link in the forward.")

                    console = Console()
                    console.print(table)


                elif command.lower() == 'back':
                    main()

                elif httppannel_input == "run":
                    fuck = self.options["PORT"]
                    shit = self.options["REGION"]
                    other = shit.lower()
                    os.system(f".\\ngrok.exe --region {other} http {fuck}")

                elif command.lower() == 'exit':
                    print(Style.BRIGHT + Fore.RED + 'Peace homie')
                    exit()
        
        
            except KeyboardInterrupt:
                continue
            except IndexError:
                return self.HTTPpannel()

            return self.HTTPpannel()

class Authtoken:
    

    def AuthtokenPannel(self):

        session = PromptSession(
                lexer=PygmentsLexer(SqlLexer), completer=Authtoken_complete)

        while True:
            print("""After installing Ngrok you'll need to connect your account. Type "token" to allow the script to be authorized.""")
            try:
                Authtoken_input = session.prompt('TKN~# ')
                parsed_token_input = Authtoken_input.split() # split the input into seperate items in a list for easier access
                command = parsed_token_input[0].lower() # setting the first item of parsed input (most likeley "set") to a seperate variable
                # checking the executed command

                if 'token' in command:
                    token_authorize = Authtoken_input[6:]
                    print(token_authorize)
                    os.system(f".\\ngrok.exe config add-authtoken {token_authorize} ")

                elif command.lower() == 'exit':
                    print(Style.BRIGHT + Fore.RED + 'Peace homie')
                    exit()

                elif command.lower() == 'help':  # you only use f strings if you are going to print a function or call another variable within a statement for examples os.system(f"cd C:\\{your_directory}")
                    table = Table(title="How to Authenticate ngrok using this script")
                    table.add_column("TYPE", justify="right", style="Green", no_wrap=True)
                    table.add_column("Instruction", style="Red")
                    table.add_row("Simple Explanation", "This pannel is ment to help with authenticating your ngrok so it works well.")
                    table.add_row("Step 1", "Go onto the offical Ngrok website, 'ngrok.com', and either sign up or login.")
                    table.add_row("Step 2", "After signing up or logining in, get the authorization code. Afterward, either paste the full string given into ngrok. Or type 'token' here and only input the end part with the code.")
                    table.add_row("Step 3", "And that it.")
                                
                    console = Console()
                    console.print(table)    

                elif command.lower() == 'back':
                    main()
        
            except KeyboardInterrupt:
                continue
            except IndexError:
                return self.AuthtokenPannel()

            return self.AuthtokenPannel()

class helppannel:
    
    def help(self):
        session = PromptSession(
            lexer=PygmentsLexer(SqlLexer), completer=help_autocomplete)

        while True:
            print("""After installing Ngrok you'll need to connect your account by using the token given on the ngrok website. Also make sure the ngrok program itself is in the same folder as this script, otherwise this will not work.""")
            
            table = Table(title="How to Set up Auto Ngrok")
            table.add_column("STEP", justify="right", style="Green", no_wrap=True)
            table.add_column("Explanation", style="White")
            table.add_column("Further Explanation", style="Red" )

            table.add_row("Step 1", "Put ngrok into the same folder as this script.", "Ngrok might be in the folder alongside the script, but if it doesn't work try deleting the ngrok and reinstalling it on the offical Ngrok website." )
            table.add_row("Step 2", "Sign up on the offical ngrok website, or login to get the authenication token")
            table.add_row("Step 3", "Either copy and paste the string given on the website into gnrok or use the Authentication", "Type 'back' and 'select SETUP'.")
            table.add_row("Step 4", "If you need help with the script, type 'help' on in the authentication tab.", "Select any of the individual options, and type 'help' anytime to see what to do.")
                   
            console = Console()
            console.print(table)
            
            try:
                help_input = session.prompt('HLP~# ')
                parsed_help_input = help_input.split() # split the input into seperate items in a list for easier access
                command = parsed_help_input[0].lower() # setting the first item of parsed input (most likeley "set") to a seperate variable
                # checking the executed command

                if command.lower() == 'exit':
                    print(Style.BRIGHT + Fore.RED + 'Peace homie')
                    exit()

                elif command.lower() == 'back':
                    main()

            except KeyboardInterrupt:
                continue
            except IndexError:
                return self.help()

            return self.help()
    

def time_start():
    time.sleep(0.01)


def main():
    for _ in track(range(100), description='[red]LOADING AUTO NGROK'):
        time_start()


    main_func_autocomplete = WordCompleter([
        'back', 'exit', 'select', 'SETUP', 'TCP/GENERIC/HOSTING', 'HTTP', 'SCRIPT-HELP',
        'GAME-HOSTING'], ignore_case=True)

    say_current_user_running = os.getenv("UserName")
    say_current_user_running_var = f'WELCOME {say_current_user_running}!'.center(100)
    print(Style.BRIGHT + Fore.RED + f'🐻{say_current_user_running_var}🐻')

    table = Table(title="AUTO NGROK")
    table.add_column("TYPE", justify="right", style="cyan", no_wrap=True)
    table.add_column("DESCRIPTION", style="magenta")

    table.add_row("*TCP*", f"SET UP TCP TUNNEL")
    table.add_row("*HTTP*", f"SET UP HTTP TUNNEL")
    table.add_row("*SETUP*", f"CONNECT YOUR NGROK TO YOUR NGROK ACOOUNT, NEEDS TO BE DONE FIRST FOR FIRST TIMERS OR REINSTALLS")
    table.add_row("*GAME HOST*", f"OPENS TUNNELS FOR GAMES THAT CAN HOST ON A LOCAL NETWORK")
    table.add_row("*HELP*", "SCRIPT SETUP INSTRUCTION")

    console = Console()
    console.print(table)


    session = PromptSession(
                lexer=PygmentsLexer(SqlLexer), completer=main_func_autocomplete)
    while True:
        try:
            current_dir = os.getcwd()
            os.chdir(current_dir)
            command = session.prompt('autongrok~# ')
    
        except KeyboardInterrupt:
            continue
        except EOFError:
            break

        if command == 'select TCP/GENERIC/HOSTING':
            owo = tcppanel()
            owo.tcpmain()

        elif command == 'select HTTP':
            owo = SmallHttpPeen()
            owo.HTTPpannel()

        elif command == 'select GAME-HOSTING':
            owo = Minecraft()
            owo.minefractSRV()

        elif command == 'select SETUP':
            owo = Authtoken()
            owo.AuthtokenPannel()
        
        elif command == 'select SCRIPT-HELP':
            owo = helppannel()
            owo.help()
        
        elif command.lower() == 'exit':
            print(Style.BRIGHT + Fore.RED + 'Peace homie')
            exit()
    

        else:
            print(Style.BRIGHT + Fore.RED + 'You entered:', command)

if __name__ == '__main__':
    main() ## if the function is called "main" then it will run that current function