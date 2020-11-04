### Guión del video transcrito:
##### Transcribed video:

---

Buenos días yo soy Pablo Corbalán y hoy os voy a contar mi experiencia después de 2 semanas utilizando Vim como editor de texto

Vim es un editor de texto integrado en la consola de un equipo, esto significa que a diferrencia de editores de código como SublimeText o Visual Studio code, para abrir Vim no tienes un icono, tienes la terminal y simplemente escribiendo "vim" lo abres. 

Esto proporciona muchas ventajas, por ejemplo vim es mucho más rápido que cualquier otro editor con una interfaz ya que no tiene que cargar ninguna librería o nada así, simplemente texto

También os digo, las comodidades que te dan editores con una interfaz son dificiles de igualar, y no es que haya un editor mejor que el otro, simplemente uno te gusta más; a mi en lo personnal me encanta Vim y tengo pensado seguir utilizándolo.

Hoy voy a hablar de como empecé a aprender Vim, y luego explicaré un poco mi configuración.

Bueno, pues este es mi editor de texto, vim; lo he estado utilizando durante exactamente 15 días para todo, incluso para algunas cosas del instituto, y lo he estado configurando bastante

Antes de empezar a ver la configuración de Vim, he creado un repositorio en mi perfil de GitHub donde voy a subir toda la configuración relaccionada con Vim, por lo que como es posible que la configuración que tengo ahora vaya mejorando, lo iré subiendo ahí.

Vale, dicho esto vamos a empezar por las cosas más básicas. Los comandos de vim son los mismos que vienen por defecto, el :w, el :q el :q! y todos esos. Y he dejado las teclas de los modos por defecto, es decir te mueves a la derecha con la "L", a la izquierda con la "H", la "J" y la "K" para abajo y para arriba etc etc... Aunque sinceramente me estoy planteando hacer alguna modificación para el modo visual del editor, para copiar y pegar texto y todo eso de forma más sencilla.
Tengo toda la configuración en el archivo .vimrc de la raiz. El archivo en sí no es mío, es una de las muchas plantillas que hay pero yo lo he ido modificando a mi gusto. Por ejemplo para todo el tema plugins los separé en este archivo `plugins.vim` de dentro de la carpeta .vim; y asi lo tengo mucho más ordenado.

Como gestor de Plugins uso Vundle, no estoy seguro de por que pero vimplug me daba problemas de vez en cuando así que he estado usando Vundle desde entonces y muy contento la verdad. Como plugins ahora mismo tengo instalados:

Vim fugitive, que es un plugin para mejorar la integración de Git en Vim, aunque aún no le he sacado todo el provecho que puedo, nerdtree para ver los archivos que es esto que veis a la izquierda de la pantalla y yo lo considero un plugin super necesario, delimitMate, que es un plugin para que los parentesis y brackets y comillas y todo eso se cierren solos...; por ejemplo veís, si yo escribo unos paréntesis o algo así se cierran solos. También tengo python-mode, que le añade a Vim un montón de información de Python, información sobre los estándares de pep8 y las "buenas practicas" de Python. fzf, que es un plugin también muy útil para explorar archivos y moverse rápido entre ellos, python-syntax, para que el código en Python se subraye bien y que todo tenga los colores que debe, Drakula que es el tema de color que estáis viendo en la pantalla, y por último emmet, que es un plugin yo diría que imprescindible si escribes algo en HTML o haces algo de web.

Si seguimos revisando el archivo `.vimrc`, después de cargar todos los plugins vemos como cambiamos un par de cosas más, como encender la sintaxis y todo eso, después cambiamos el tamaño de los idents y de los espacios y poco más, aquí decimos que se vean los numeros de línea, y aquí por último decimos que al cargar vim abrá nerd tree automáticamente.

Te recuerdo que tienes toda la configuración en un enlace que te dejaré en la descripción y que tenemos un servidor de discord donde estaré encantado de hablar contigo.

Si te ha gustado el video dejamé un comentario, que es lo que más agradezco y nos vemos!
