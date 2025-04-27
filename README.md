
# Research Project para Odoo 18

## Descripción

Este módulo permite gestionar proyectos de investigación en Odoo 18. Los usuarios pueden:

- Crear y administrar proyectos.
- Asignar investigadores.
- Cambiar estados del proyecto (Nuevo, En Progreso, En Revisión, Completado, Cancelado).
- Calcular automáticamente la duración del proyecto.
- Generar reportes en PDF con todos los detalles, incluyendo la lista de investigadores asociados.

---

## Dependencias

- **Odoo 18**
- **Módulos requeridos:** `base`, `mail`, `report`

---

## Instalación

1. **Clona o descarga el módulo:**
   - Coloca la carpeta `research_project` en el directorio de addons personalizados de Odoo (por ejemplo:  
     `C:\odoo\odoo\custom_addons\`).

2. **Actualiza la ruta de addons:**
   - Asegúrate de que tu archivo `odoo.conf` incluya la ruta de addons personalizados:
     ```ini
     [options]
     addons_path = C:\odoo\odoo\addons,C:\odoo\odoo\custom_addons
     ```

3. **Inicia Odoo y actualiza la lista de aplicaciones:**
   - Inicia Odoo con la base de datos deseada:
     ```bash
     python c:/odoo/odoo/odoo-bin -c c:/odoo/odoo.conf -d <nombre_base_datos>
     ```
   - Ve a **Apps** en Odoo y haz clic en "Actualizar lista de aplicaciones".

4. **Instala el módulo:**
   - Busca "Research Project" en Apps y haz clic en **Instalar**.

5. **Instalación alternativa por línea de comandos:**
   ```bash
   python c:/odoo/odoo/odoo-bin -c c:/odoo/odoo.conf -d <nombre_base_datos> -i research_project --stop-after-init
   ```

---

## Uso

1. Ve a **Proyectos de Investigación > Proyectos** en el menú de Odoo.
2. Haz clic en **Nuevo** para crear un proyecto.
3. Llena los detalles del proyecto (nombre, fechas, presupuesto, investigador principal, etc.).
4. Usa los botones de estado (por ejemplo, "Iniciar", "Enviar a Revisión") para gestionar el ciclo de vida del proyecto.
5. Comunícate a través del chatter añadiendo mensajes o programando actividades.
6. Genera un informe seleccionando un proyecto y haciendo clic en **Action > Informe de Proyecto de Investigación**.

---

## Funcionalidades

- Crear y gestionar proyectos de investigación con campos como nombre, código, descripción, fechas, presupuesto y prioridad.
- Gestionar estados del proyecto: **Nuevo**, **En Progreso**, **En Revisión**, **Completado**, **Cancelado**.
- Relacionar un investigador principal y múltiples investigadores (usando `res.partner`).
- Cálculo automático de la duración del proyecto en días basado en las fechas de inicio y fin.
- Validación de fechas para asegurar que la fecha de inicio sea anterior a la de finalización.
- Secuencia automática para generar códigos de proyecto (ejemplo: `PR0001`).
- Comunicación a través del chatter de Odoo (mensajes y actividades).
- Generar un informe en PDF con todos los detalles del proyecto, incluyendo la lista de investigadores.
- **Seguridad:** Grupos de usuarios para controlar accesos (usuarios solo ven sus propios proyectos, gerentes ven todos).

---

## Estructura de Archivos

- `models/research_project.py`: Define el modelo `research.project` y su lógica.
- `views/research_project_views.xml`: Contiene las vistas de formulario, lista y búsqueda.
- `report/report_research_project.xml`: Define el informe QWeb para los proyectos.
- `security/`: Configuraciones de seguridad y derechos de acceso.
- `data/`: Secuencia para los códigos de los proyectos.

---

## Consideraciones Técnicas

- Se utiliza `@api.constrains` para validar que la fecha de inicio sea anterior a la de finalización.
- Se utiliza `@api.onchange` para limpiar la fecha de finalización si la fecha de inicio es posterior.
- Se utiliza `@api.depends` para calcular automáticamente la duración del proyecto.
- Se creó un grupo de seguridad específico para controlar accesos: usuarios ven solo sus proyectos, mientras que los gerentes ven todos.

---

## Mejoras Potenciales

- Agregar gráficos de avance de proyectos para visualizar el progreso.
- Crear tareas o hitos asociados al proyecto para un seguimiento más detallado.

---

## Autor

**Gustavo Seijas**

---

## Soporte

Para problemas o sugerencias, por favor contacta al autor.
