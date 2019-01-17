grammar cev;

stmt: resistor;

resistor: value=NUMBER UNIT_RESISTOR;


NUMBER: [0-9]+([.][0-9]*)?;
UNIT_RESISTOR: ('Ohm' | 'R');
WHITESPACE: ' ' ->skip;
