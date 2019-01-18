grammar cev;

stmt    : connection  | function;

function            : voltageFunction;

voltageFunction     : 'U' '(' connection parameterList ')';

connection  :   connection '+' connection   #series_connection
            |   connection '||' connection  #parallel_connection
            |   components                  #connectionComponent;

components      :   element=resistor    #resistorComponent
                |   element=voltage     #voltageSourceComponent;

parameterList   : (',' currentParameter )*;

currentParameter    : 'I' '=' parameter=current;

resistor        : value=NUMBER UNIT_RESISTOR;


voltage  :  value=NUMBER UNIT_VOLTAGE;
current  :  value=NUMBER UNIT_CURRENT;

NUMBER: [0-9]+([.][0-9]*)?;
UNIT_RESISTOR: ('Ohm' | 'R');
UNIT_VOLTAGE:   'V';
UNIT_CURRENT:   'A';
WHITESPACE: ' ' ->skip;
