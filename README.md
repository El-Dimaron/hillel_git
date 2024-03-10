The following function is used for generating password (surprisingly, I know).

The difficulty/reliability of the password can be increased by passing the following arguments into the function 'def password_gen':
- letters - if True, both upper and lower registers will be used, if False - only lower ones (default, False);
- symbols - if True, the following symbols will be added to the password "!@#$%^&*()+" (default, False);
- numbers - if True, adds numbers (0-9) to the password (default, False);
- duplicates - if True, only unique elements will be used, no repetition (default, False);
- pass_length - determines the length of the password (default, 8).

Note: when it is necessary to create a unique-element password (duplicates=True), please do not set pass_length to a value higher than 30, as the password might run out of unique elements and the function will display an error.

Enjoy the code and have a calm evening!