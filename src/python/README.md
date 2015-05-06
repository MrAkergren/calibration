Code structure
===
Main files.
---
|File | Contains |
| --- | --- |
|```main.py``` | The algorithms and logic. |
|```serial_handler.py```| The class that acts as an interface between the serial communication and ```main.py```
|```serial_com.py```| The class for communication over the serial interface. |
|```arduino.py``` | inherit form  ```serial_com.py```, holds the methods specific for the lux-meter, such as "get_value" |
|```panel.py```|  inherit form  ```serial_com.py```, holds the methods specific for panel, such as "move" |
|```mock_read.py``` | file is used to pull values when the lux-meter is not available. |
|```__init.py__``` | is needed by the language. |

Legacy
---
Files used previous during the development

Style guide for Python source code 
===
|Type  |  Public | Internal |
|--- | --- | --- | 
|Packages |   lower_with_under    ||
|Modules   |  lower_with_under |   _lower_with_under |
|Classes   |  CapWords  |  _CapWords |
|Exceptions | CapWords    ||
|Functions  | lower_with_under() | _lower_with_under() |
|Global/Class Constants | CAPS_WITH_UNDER |    _CAPS_WITH_UNDER |
|Global/Class Variables | lower_with_under |   _lower_with_under |
|Instance Variables | lower_with_under  |  _lower_with_under (protected) or __lower_with_under (private) |
|Method Names  |  lower_with_under() | _lower_with_under() (protected) or __lower_with_under() (private) |
|Function/Method Parameters | lower_with_under    ||
|Local Variables   |  lower_with_under    ||

For more information see: https://google-styleguide.googlecode.com/svn/trunk/pyguide.html
