grammar cev;

stmt: connection;

connection  : connection '+' connection #series_connection
            | resistor              #element;

resistor: value=NUMBER UNIT_RESISTOR;


NUMBER: [0-9]+([.][0-9]*)?;
UNIT_RESISTOR: ('Ohm' | 'R');
WHITESPACE: ' ' ->skip;
