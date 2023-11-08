import openai
#DIRECCION DE OPENAI QUE TE DA ACCESO AL MODELO POR AUTENTICACION
openai.api_key = #insertar aqui entre comillas
chatHistory = []
collected_messages = []

def procesarPregunta():
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = chatHistory,
    Stream = True #Para activar recepcion de la informacion por partes
    maxTokens=100 #Cantidad maxima de tokens por solicitud    
                                                                        
    )
        chat_history.append({"role": "user", "content": prompt})
def Mostrarenpantalla:
    for parte in response:
            parte_message = parte['choices'][0]['delta']  # extraear parte del mensaje que intersa dentro del onjeto que se recibe
            collected_messages.append(parte_message)  #juntar las partes para luego imprimir
            full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
            print(full_reply_content)
    # limpiar terminal
            print("\033[H\033[J", end="")
            
    chat_history.append({"role": "assistant", "content": full_reply_content}) #Agregar mensaje del asistente al historial
        # imprimir todo lo recibido hasta el momento
        full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
        print(f"GPT: {full_reply_content}")
        
def chatear():
    procesarPregunta()
    Mostrarenpantalla()
    
while True:
    prompt = input("Enter a prompt: ")
    if prompt == "exit":
        break
    else:
        chatear():

        
"""
La respuesta se entrega como un objeto, dentro de choices se encuentran los mensajes, que tambien es otro objeto
el index 0 es el primer mensaje del chat, y dentro content, es donde esta el contenido de ese mensaje especifico

print(response["choices"][0]["messages"]["content"]) es para esperar a recibir todo el mensaje y lugo mostrarlo
pero el indice debe variar segun el mensaje que se muestre, de decantarnos por esta opcion habria que modificarlo
en la funcion Mostrarenpantalla()

SI SE QUIERE HACER IMPRESION PROGRESIVA EN PANTALLA LA LOGICA SERIA LA SIGUIENTE.
"""
    

