import sys


class MarkDownEditor:
    help_command_text = '''
Available formatters: plain bold italic header link inline-code ordered-
list unordered-list new-line
• plain — обычный текст без форматирования
• bold/italic — полужирный/курсив
• inline-code — встроенный код
• link — ссылка
• header — заголовок
• unordered-list — неупорядоченный список
• ordered-list — упорядоченный список
• new-line — переход на новую строку.
Special commands: !help !done'''
    def __init__(self) -> None:
        self.markdown_text = ''

        while True:
            formatter_choice = {
                'plain': self.plain,
                'bold': self.bold,
                'italic': self.italic,
                'inline-code': self.inline_code,
                'link': self.link,
                'header': self.header,
                'unordered-list': self.unordered_list,
                'ordered-list': self.ordered_list,
                'new-line': self.new_line,
                '!help': self.help,
                '!done': self.done
            }

            formatter = input('Choose a formatter:')

            if formatter not in formatter_choice.keys():
                print(f'There is no {formatter} in available options')
                continue

            formatter_func = formatter_choice.get(formatter)
            formatter_func()

            print(self.markdown_text)

    def done(self):
        with open('simplified-markdown-editor/output.md', mode='w') as f:
            f.write(self.markdown_text)

        sys.exit()

    def help(self):
        print(self.help_command_text)

    def get_text(self):
        return input('Input your text:')

    def get_row_count(self):
        while True:
            try:
                row_count = int(input('Input count of rows: '))

                if row_count < 1:
                    print('Should be greater than 0')
                    continue

                return row_count
            except Exception:
                print('Should be integer')

    def get_level(self):
        while True:
            try:
                level = int(input('Enter the level of header:'))

                if level < 1 or level > 6:
                    print('Should be within 1 to 6')
                    continue
                    
                return level
            except Exception:
                print('Should be integer')

    def plain(self):
        text = self.get_text()
        self.markdown_text += f'{text}'
    
    def bold(self):
        text = self.get_text()
        self.markdown_text += f'**{text}**'
    
    def italic(self):
        text = self.get_text()
        self.markdown_text += f'*{text}*'
    
    def inline_code(self):
        text = self.get_text()
        self.markdown_text += f'`{text}`'
    
    def link(self):
        label = input('Label:')
        link = input('Link:')
        self.markdown_text += f'[{label}]({link})'
    
    def header(self):
        text = self.get_text()
        level = self.get_level()
        self.markdown_text += f'\n{"#" * level}{text}\n'

    def ordered_list(self):
        row_count = self.get_row_count()

        for i in range(1, row_count+1):
            text = input(f'Row#{i}: ')
            self.markdown_text += f'{i}. {text}\n'
    
    def unordered_list(self):
        row_count = self.get_row_count()

        for i in range(1, row_count+1):
            text = input(f'Row#{i}: ')
            self.markdown_text += f'- {text}\n'

    def new_line(self):
        self.markdown_text += '\n'

if __name__ == "__main__":
    MarkDownEditor()