 # JERRY (Voice Control Personal-Virtual-Assistant)

# Libraries Used in Jerry - Virtual Assistant

**pyttsx3:**

A text-to-speech conversion library in Python. It allows Jerry to speak responses, providing an auditory interaction with users.

**speech_recognition:**

A library that enables Jerry to recognize and process spoken language. It converts speech input from the user into text, allowing for natural language interaction.

**datetime:**

A module that supplies classes for manipulating dates and times. Jerry uses this library to determine the current date and time for greeting users, setting alarms, and timestamping notes.

**webbrowser:** 

A standard library module that provides a high-level interface for displaying web-based documents. Jerry uses it to open websites and perform web searches.

**pywhatkit:** 

A library used to automate WhatsApp messages, play YouTube videos, and perform Google searches. It enhances Jerry's communication and entertainment capabilities.

**pyjokes:** 

A library that provides random jokes, adding a fun and interactive element to Jerry's responses.

**os:** 

A standard library module that provides a way of using operating system-dependent functionality like reading or writing to the file system. Jerry uses it to manage files and directories, such as saving notes.

**time:** 

A standard library module that provides various time-related functions. Jerry uses it for tasks that require time manipulation, such as setting alarms or delays.

**wikipedia:** 

A library that allows Jerry to search for and retrieve summaries of Wikipedia articles, providing users with information on a wide range of topics.

**pyautogui:** 

A library used to programmatically control the mouse and keyboard. Jerry uses it for automating system navigation tasks like opening and closing applications.

**wolframalpha:** 

A library for accessing the Wolfram Alpha computational engine. Jerry uses it to answer factual queries and perform complex calculations.

**requests:** 

A library for sending HTTP requests. It can be used for interacting with web APIs, downloading content, or performing web scraping.

**playsound:** 

A simple library for playing sound files. Jerry uses it to play audio responses or notifications.

**re:** 

A library for regular expressions, used for string matching and manipulation. Jerry uses it to parse and process text data, such as cleaning input or extracting information.

**translate:** 

A library that provides translation services, enabling Jerry to translate text between different languages.

**json:** 

A standard library for parsing JSON (JavaScript Object Notation). Jerry uses it to handle data storage and retrieval in a structured format.

**pandas:** 

A data manipulation and analysis library. It is used in Jerry for managing and processing data, particularly in tasks like handling user inputs or managing note files.


# Summary of Jerry's Functionalities

1. Initialization and Text-to-Speech (TTS) Setup:

     Utilizes pyttsx3 for text-to-speech capabilities, allowing Jerry to vocalize responses.
   
     Configures voice settings to customize the speaking voice.
   
2. Greeting and Day Identification:

     wishMe(): Greets the user based on the current time (morning, afternoon, evening).
   
     tellDay(): Provides information about the current day of the week.

3. Speech Recognition:

     get_audio(): Captures audio input from the user and converts it to text using speech_recognition.
   
     takeCommand(): Listens for commands from the user, processes them, and executes appropriate actions.

4. Security Check:

     Implements a password prompt to ensure secure access to the assistant's functionalities.

5. Alarm Functionality:

     alarm(): Allows users to set alarms, storing alarm times and triggering an alarm script at the set time.

6. Movie Information Search:

     search_movie(): Retrieves movie information from the IMDb database, providing details such as title, release year, rating, and plot summary.

7. Computational Queries and Calculations:

     WolfRamAlpha(): Answers complex queries and performs calculations using the Wolfram Alpha computational engine.
   
     Calc(): Handles arithmetic and logical operations.

8. Messaging Service:

     sendMessage(): Sends messages via WhatsApp using pywhatkit, allowing for automated communication.

9. Note Taking:

     Allows users to write and view notes, with the option to timestamp entries for organizational purposes.

10. Translation:

     Translates text between different languages using a translation service, enhancing communication capabilities.

11. Web and System Navigation:

     webbrowser and pyautogui: Automate opening and closing web pages, perform searches, and navigate system interfaces.
   
     Commands include opening YouTube, Google searches, file explorer, settings, and task management.

12. Google Chrome Control:
 
     Open Tab: Opens a new tab in Google Chrome.
   
     Open History: Navigates to the browser's history page.
   
     Open Downloads: Opens the downloads page in Chrome.
   
     Clear History: Clears browsing history.
   
     Previous/Next Tab: Switches between open tabs.
   
     Close Tab: Closes the current tab in Chrome.

13. Application Control:

     Opens and closes specific applications like Visual Studio Code and Command Prompt, enhancing productivity.

14. Volume Control:

     Volume Up: Increases the system volume.
   
     Volume Down: Decreases the system volume.
   
     Mute: Mutes the system volume.

15. Temperature Information:

     Temperature: Provides current temperature information, potentially integrating with an online weather service to give accurate and up-to-date weather      
                  conditions.

16. News Updates:

     News: Fetches the latest news headlines and summaries from various news sources. This feature provides users with a quick update on current events, covering 
           various categories such as world news, technology, entertainment, sports, and more.

17. Internet Speed:

     Internet Speed: Measures and provides information about the current internet speed, including download and upload speeds. The measurement is approximate, not 
                     overly precise but sufficient for general use.

18. Jokes:

    Joke: Provides a random joke to entertain users, adding a fun element to the interaction.

19. Random Facts:

     Random Facts: Shares interesting and random facts with users, offering informative and engaging tidbits.

20. IP Address:

     IP Address: Displays the public IP address of the user's system, useful for identifying network details.

21. System Management:

     Shutdown: Initiates a system shutdown, turning off the computer.
   
     Sleep: Puts the computer into sleep mode, conserving energy while maintaining system state.
   
     Restart: Restarts the computer, closing all applications and rebooting the system.

22. Miscellaneous Features:

     Play Introductory GIF: Uses an external function to play a GIF, providing a visual element to interactions.
   
     Stone-Paper-Scissor Game: A fun interactive game feature that allows users to play a classic game with the assistant.
   
     Schedule My Day with Notification Sound: Helps users plan their day by setting reminders and playing notification sounds to alert them at specific times.





This detailed summary outlines the extensive range of features available in Jerry, highlighting its versatility as a multifunctional virtual assistant.
