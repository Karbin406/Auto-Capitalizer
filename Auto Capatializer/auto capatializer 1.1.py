import sys
import time
import datetime
import re
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
from PyQt5.QtGui import QIcon, QFont, QPainter, QPixmap, QImage
from PyQt5.QtCore import Qt
from bs4 import BeautifulSoup





class AutoCapitalizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto Capitalizer")
        self.setGeometry(50, 50, 1600, 900)
        
        self.label1 = QLabel("Auto Capitalizer, please enter text and keywords via the terminals", self)
        self.label2 = QLabel("Your capitalized article are there")
        self.Result_display = QTextEdit(self)
        
        
        self.backgroundimage = QPixmap("E:\VScode\HTML\images\geblctaaisedf.png")
        self.initUI()
        
    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.Result_display)
        self.setLayout(vbox)
        
        self.setStyleSheet("""
        QLabel {
            font-size: 30px; 
            font-family: IBM Plex Mono;
            }
            
        QTextEdit {
            font-size: 20px;
            font-family: IBM Plex Mono;
            }""")
        
        self.Result_display.setPlaceholderText("Your capitalized article will be displayed here")
    
    def paintEvent(self, a0):
        resized_background = self.backgroundimage.scaled(self.size(), aspectRatioMode=1)
        painter = QPainter(self)
        painter.drawPixmap(0, 0, resized_background)
        
    def setText(self, text):
        self.Result_display.setText(text)

#above are for PyQt5 GUI

    def report(cap_word, key_word_count):
        """
        Generate a report of the capitalization process
        
        :cap_word: The word that is being capitalized
        :key_word_count: The number of times the word is found in the article
        """
        print(f'\nThere are total [{key_word_count}] "{cap_word}" found in your article\n')

    def main():
        now = datetime.datetime.now()
        now = now.strftime("{%Y-%m-%d %H-%M-%S}\n")
        log_path = "E:\\VScode\\Python\\Shitty personal project\\Auto Capatializer\\log.txt"

        try:
            cap_times = int(input('\nHow many words you need to capitalize?\n\n'))

        except ValueError:
            print('You may type some words for the capitalize times, remember to type your words first')
            with open(log_path, 'a', encoding="utf-8") as file:
                file.write(f"\n{now}\n")
                file.write("User typed str object for the cap_times which was supposed to receive int object as input")
                file.write(f"\n                         //////ValueError occurred//////\n\n\n\n")
            sys.exit(1)

        time.sleep(1)
        article = input('''\n# Input your article #
    # Make sure the word spelling is all correct! Also make sure that the word has no pre-capitalized alphabet#\n\n''')

        with open(log_path, 'a', encoding="utf-8") as file:
            file.write(f"\n{now}\n")
            file.write(f"\nThere are [{cap_times}] words that will be capitalized in the current session.")
            file.write(f"\nThis is the article that is being capitalized in the current session: \n")
            file.write(f'\n-----------------------')
            file.write(f'\n{article}\n')
            file.write(f'----------------------\n\n\n')

        time.sleep(2)
        print("\nYour words are successfully inputted")   

        if 'hatsune miku' in article:
            time.sleep(1.5)
            print('hatsune miku does not talk to British people (｡ ˇ‸ˇ ｡)\n')

        words_to_capitalize = []
        for i in range(cap_times):
            time.sleep(1)
            cap_word = input(f'''
            # Input the keyword {i + 1} you want to capitalize #
            ''').strip()

            with open(log_path, 'a', encoding="utf-8") as file:
                file.write(f"\nThis is the [{i + 1}] word that is being capitalized in the current session: \n")
                file.write(f'\n         [{cap_word}]\n')

            # Create a regex pattern to match the whole word only
            pattern = r'\b' + re.escape(cap_word) + r'\b'

            # Search for the word in the article
            matches = list(re.finditer(pattern, article, re.IGNORECASE))

            if matches:
                # Capitalize the found words
                for match in matches:
                    start, end = match.span()
                    article = article[:start] + article[start:end].upper() + article[end:]

                key_word_count = len(matches)
                with open(log_path, 'a', encoding="utf-8") as file:
                    file.write(f"       #This word is found\n")
                time.sleep(1)
                AutoCapitalizer.report(cap_word, key_word_count)

            else:
                time.sleep(1)
                print (f'\nCannot find your word [{cap_word}] in the article \nPlease try another word for this one\n')
                with open(log_path, 'a', encoding="utf-8") as file:
                    file.write(f"       #This word is not found\n")
                continue

        print("Currently capitalizing your article......")
        time.sleep(2)
        final_result = article
        print(f'''\nResult:  
        ''')

        with open(log_path, 'a', encoding="utf-8") as file:
            file.write(f"\n\n\nThis is the final result of the capitalization: \n")
            file.write(f'\n------------------------------')
            file.write(f'\n{final_result}\n')
            file.write(f'------------------------------\n\n\n\n\n\n\n\n\n')

        time.sleep(1)
        print(final_result)
        window.setText(final_result)
        print('\nCapitalization finished\n ')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AutoCapitalizer()
    window.show()
    AutoCapitalizer.main()
    sys.exit(app.exec_()) 

