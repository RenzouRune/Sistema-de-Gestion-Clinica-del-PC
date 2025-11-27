# TODO List for Fixing FieldError in Django App

- [x] Update Reporte.__str__ in entrega/models.py to use self.diagnostico instead of self.asignacion
- [x] Update reporte function in entrega/views.py: Change Reporte creation to use diagnostico, update existence check
- [x] Update verificar_entregas function in entrega/views.py: Fix filter to use diagnostico__asignacion__equipo__cliente, set reportes_cliente
- [x] Update comprobante function in entrega/views.py: Fix filter for entrega to use diagnostico__asignacion__equipo
