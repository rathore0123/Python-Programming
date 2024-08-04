questions = [
    ["What does HTML stand for?", "Hyper Text Markup Language", "Hyperlinks and Text Markup Language", "Home Tool Markup Language", "Hyperlinking Textual Markup Language", "Hyper Text Markup Language"],
    ["What does CSS stand for?", "Cascading Style Sheets", "Computer Style Sheets", "Creative Style Sheets", "Colorful Style Sheets", "Cascading Style Sheets"],
    ["What is the main purpose of JavaScript?", "Styling web pages", "Structuring web pages", "Adding interactivity to web pages", "Creating databases", "Adding interactivity to web pages"],
    ["Which HTML tag is used to define an internal style sheet?", "<style>", "<script>", "<css>", "<link>", "<style>"],
    ["What is the correct syntax for referring to an external script called 'script.js'?", "<script src='script.js'>", "<script href='script.js'>", "<script link='script.js'>", "<script name='script.js'>", "<script src='script.js'>"],
    ["Which property is used to change the background color in CSS?", "bgcolor", "background-color", "color", "background", "background-color"],
    ["Which SQL statement is used to extract data from a database?", "GET", "OPEN", "EXTRACT", "SELECT", "SELECT"],
    ["What does PHP stand for?", "Personal Home Page", "Private Home Page", "PHP: Hypertext Preprocessor", "Pretext Hypertext Processor", "PHP: Hypertext Preprocessor"],
    ["What does JSON stand for?", "JavaScript Object Notation", "JavaScript Online Notation", "JavaScript Object Notifier", "JavaScript Offline Notation", "JavaScript Object Notation"],
    ["Which HTML element is used for the largest heading?", "<head>", "<h6>", "<heading>", "<h1>", "<h1>"],
    ["Which company developed the React library?", "Google", "Microsoft", "Facebook", "Twitter", "Facebook"],
    ["Which of the following is not a JavaScript framework?", "React", "Angular", "Vue", "Django", "Django"],
    ["Which of the following is used to connect to a database in Python?", "Pandas", "NumPy", "MySQL", "Matplotlib", "MySQL"],
    ["Which version control system is commonly used in software development?", "Mercurial", "Subversion", "Git", "CVS", "Git"],
    ["What does REST stand for in web development?", "Representational State Transfer", "Remote State Transfer", "Rapid State Transfer", "Reliable State Transfer", "Representational State Transfer"],
    ["What is the purpose of the 'box-sizing' property in CSS?", "To define the element's padding", "To define the element's border", "To include padding and border in the element's total width and height", "To exclude padding and border from the element's total width and height", "To include padding and border in the element's total width and height"],
    ["Which command is used to initialize a new Git repository?", "git start", "git begin", "git init", "git new", "git init"],
    ["What is the purpose of the 'use strict' directive in JavaScript?", "To enable strict mode which catches common coding mistakes", "To allow the use of global variables", "To disable error messages", "To enable faster execution", "To enable strict mode which catches common coding mistakes"],
    ["Which of the following is a CSS preprocessor?", "jQuery", "Sass", "React", "Angular", "Sass"],
    ["What is an IIFE in JavaScript?", "Immediately Invoked Function Expression", "Internally Invoked Function Expression", "Indirectly Invoked Function Expression", "Instantly Invoked Function Expression", "Immediately Invoked Function Expression"]
]

levels = [ 1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000
]

money = 0
for i in range(len(questions)):
    print(questions[i][0])
    print(f"option a: {questions[i][1]}        option b: {questions[i][2]}")
    print(f"option c: {questions[i][3]}           option d: {questions[i][4]}")
    print(f"suggestion:  {questions[i][5]}")
    answer = input("Enter answer btween 1to 4, press 5 for quit: ")
    if(answer == '5'):
        print(f"Your wining amount is {money}")
        break
    if(answer == questions[i][5]):
        money = levels[i]
        print(f"Conratulations you won Rs. {money}")
    else:
        print("Wrong Answer Better luck next time!")
        break
print(f"You won {money} Rupees  you can receive this amount in your bank account")