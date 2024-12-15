from vectordb import Memory
import re

memory = Memory(chunking_strategy={'mode':'sliding_window', 'window_size': 32, 'overlap': 4})

def tokenize( msg:str ):
    msg = msg.replace( "coche", "vehiculo" )

    ret = [ ]
    not_words = [ "", "con", "de", "y" ]
    msg = re.split("[ ,\.?]", msg)
    
    for m in msg:
        if m not in not_words:
            ret.append( m )

    print( ret )

    return " ".join( ret )

memory.save(
    tokenize( "coche de color amarillo, número de ruedas 2 y tipo terrestre" ), 
    { "title": "Título 2", "url": "https://xxx2.com" }
)

memory.save(
    tokenize( "coche de color rojo, número de ruedas 3 y tipo terrestre" ), 
    { "title": "Título 1", "url": "https://xxx1.com" }
)

memory.save(
    tokenize( "coche de color verde, número de ruedas 3 y tipo terrestre" ), 
    { "title": "Título 3", "url": "https://xxx3.com" }
)

memory.save(
    tokenize( "coche de color blanco, número de ruedas 0 y tipo acuatico" ), 
    { "title": "Título 4", "url": "https://xxx4.com" }
)

memory.save(
    tokenize( "coche de color blanco, número de ruedas 0 y tipo terrestre" ), 
    { "title": "Título 5", "url": "https://xxx5.com" }
)

memory.save(
    tokenize( "moto de color blanco, número de ruedas 2 y tipo terrestre" ), 
    { "title": "Título 5", "url": "https://xxx5.com" }
)



print(
    memory.search( tokenize( "coche con 3 ruedas y de tipo terrestre?" ), top_n=2)
)
