import ollama
import sys

def Main(argv):
    response = ollama.chat(
        model='llama3.2-vision:11b',
        messages=[{
            'role': 'user',
            'content': 'What is in this image?',
            'images': ['image.jpg']
        }]
    )

    print(response)

if(__name__ == "__main__"):
    Main(sys.argv[1:])