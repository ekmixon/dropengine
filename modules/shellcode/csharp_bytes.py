from base.shellcode.shellcode import Shellcode

class CSharpBytesShellcode(Shellcode):

    def __init__(self):

        self.name = 'csharp_bytes_shellcode'
        self.author = 's0lst1c3'
        self.description = 'Output as a byte array (hex representation)'
        super().__init__()
    
    def render(self, text):

        return self._render_helper(text)

    def _render_helper(self, text):

        rendered_text = '{\n            '
        split_chars = text.hex(' ').split()
        index = 0

        for i,c in enumerate(split_chars):

            rendered_text += f'0x{c},\n            ' if i % 10 == 9 else f'0x{c}, '
        rendered_text = rendered_text[:len(rendered_text)-2] + '\n        }'

        return rendered_text
