Code structure
===
Main files.
---
|File | Contains |
| --- | --- |
|```main.py``` | The startup file, just contains functions to start the application. |
|```serial_handler.py```| The class that acts as an interface between the serial communication and other classes|
|```serial_handler_arr.py```| The class that acts as an interface between the array and other classes (for testing)|
|```serial_com.py```| The class for communication over the serial interface. |
|```arduino.py``` | inherit form  ```serial_com.py```, holds the methods specific for the lux-meter, such as "get_value" |
|```panel.py```|  inherit form  ```serial_com.py```, holds the methods specific for panel, such as "move" |
|```yocto_lux.py``` | contains the methods for the Yocto lux-meter, does not inherit from ```serial_com``` as it doesn't require RS-232 |
|```search.py```| The class for the search algorithm |
|```gui``` | package containing the two gui files, one for the controls and one to check if the application is running on windows|
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
