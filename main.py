import dearpygui.dearpygui as dpg
from screeninfo  import get_monitors
import funciones as fs
a = get_monitors()
alto = a[1].height
ancho = a[1].width
celdasx = ancho/12
celdasy = alto /30

#eventos
def __buscarClick():
    codigo = dpg.get_value("Codigo_label")
    nombres = dpg.get_value("Nombres_label")
    apellidos = dpg.get_value("Apellidos_label")
    
    print(codigo,nombres,apellidos)
    response = fs.pedirvalor(codigo,nombres,apellidos)
    valor = 0
    for i in response:
        valor += i[2]
    print(valor)
    dpg.set_value("monto", f"{valor}")
    for i in response:
        with dpg.table_row(parent= tba):
            dpg.add_text(i[0])
            dpg.add_text(i[1])
            dpg.add_text(i[2])
    

dpg.create_context()

dpg.create_viewport(title="Pantalla",width=ancho, height=alto,resizable=False)
dpg.setup_dearpygui()

with dpg.window(tag="Principal", no_title_bar=True, pos=[0,0], width=ancho, height=alto, no_resize=True, no_move=True):
    with dpg.group():
        dpg.add_text("Codigo", color=[255,255,255], pos=[(celdasx*3)-50, (celdasy*4)])
        
        dpg.add_text("Nombres", color=[255,255,255], pos=[(celdasx*6)-50, (celdasy*4)])
        dpg.add_text("Apellidos", color=[255,255,255], pos=[(celdasx*9)-50, (celdasy*4)])
        dpg.add_input_text(width=celdasx*2, pos=[(celdasx*2), (celdasy*5)], tag="Codigo_label")
        dpg.add_input_text(width=celdasx*2, pos=[(celdasx*5), (celdasy*5)], tag="Nombres_label")
        dpg.add_input_text(width=celdasx*2, pos=[(celdasx*8), (celdasy*5)], tag="Apellidos_label")
        dpg.add_button(label="Buscar" ,width=celdasx/2, pos=[(celdasx*10.5),(celdasy*5)], callback= __buscarClick)
    
    with dpg.group(pos=[(celdasx*2), (celdasy*11)], width=celdasx*8, height=celdasy*14):
        with dpg.table( tag="Taba_Mustra",header_row=True, resizable=True,
                            borders_outerH=True, borders_innerH=True, 
                            borders_outerV=True, delay_search=True) as tba:
            
            dpg.add_table_column(label="Descripcion")
            dpg.add_table_column(label="Año")
            dpg.add_table_column(label="Monto")
    
    with dpg.group():
        dpg.add_input_text(default_value="0", pos=[(celdasx*7),(celdasy*27)], width=celdasx*2, tag= "monto")
            
            



dpg.show_viewport()
dpg.start_dearpygui()

dpg.destroy_context()


