grammar cev;

stmt: connection | voltage;

connection  :   connection '+' connection   #series_connection
            |   connection '||' connection  #parallel_connection
            |   resistor                    #element;

resistor: value=NUMBER UNIT_RESISTOR;
voltage:  value=NUMBER UNIT_VOLTAGE;


NUMBER: [0-9]+([.][0-9]*)?;
UNIT_RESISTOR: ('Ohm' | 'R');
UNIT_VOLTAGE:   'V';
WHITESPACE: ' ' ->skip;
