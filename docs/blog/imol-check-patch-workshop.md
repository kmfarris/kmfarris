# IMOL: letting AI assistants write code safely

AI coding assistants are good at producing code, but the way that code reaches your files is crude. The assistant writes text, the text is pasted into a file, and mistakes surface later, sometimes after the program has already changed files or reached out over the network.

IMOL is a programming language built around a safer sequence of steps.

## 1. Check the program first

Before any change is saved, IMOL checks the program for mistakes. The problems come back in a structured form the assistant can read, such as "this function is missing a value here," so the assistant can fix its own errors instead of guessing from a wall of error text.

## 2. Edit by name, not by line number

Every part of an IMOL program can carry a permanent name tag. Instead of "replace lines 40 to 62," the assistant says "replace the function tagged with this name." If the file is reformatted or something is added above, the edit still lands in the right place.

## 3. Declare what the program may do

Each IMOL program states up front what it's allowed to do: read files, write files, use the internet, or run system commands. Anything it hasn't declared, it can't do.

## 4. Rehearse before acting

IMOL can run a program as a rehearsal. It records every action the program would take, such as reading this file or writing that one, without actually doing any of them. Someone can review the list, and the real actions only run after explicit approval.

## Where it stands

All of these pieces work, the automated tests pass, and IMOL connects to the Cursor code editor so an assistant there can run the checks itself. The remaining work is housekeeping: bringing two internal version numbers back in line, publishing IMOL as an installable package, and writing a formal definition of the language.

```bash
git clone https://github.com/kmfarris/imol
cd imol
npm install && npm run build
npm run imol -- agent check examples/dogfood/catalog.imol
```

Source: [github.com/kmfarris/imol](https://github.com/kmfarris/imol)
