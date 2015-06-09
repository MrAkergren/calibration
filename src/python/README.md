Code structure
===
Packages
---
|Folder | Contains|
| --- | ---|
| gui | two gui files, one for the controls and one to check if the application is running on windows|
| legacy | Files used previous during the development |
| test | Files for testing of the algorithms|

Main files
---
|File | Contains |
| --- | --- |
|```__init.py__``` | is needed by the language. |
|```arduino.py``` | inherit form  ```serial_com.py```, holds the methods specific for the lux-meter, such as "get_value" |
|```main.py``` | The startup file, just contains functions to start the application. |
|```panel.py```|  inherit form  ```serial_com.py```, holds the methods specific for panel, such as "move" |
|```search.py```| The class for the search algorithm |
|```serial_com.py```| The class for communication over the serial interface. |
|```serial_handler.py```| The class that acts as an interface between the serial communication and other classes|
|```yocto_lux.py``` | contains the methods for the Yocto lux-meter, does not inherit from ```serial_com``` as it doesn't require RS-232 |


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
