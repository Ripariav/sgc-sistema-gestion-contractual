#!/usr/bin/env python
"""Script para poblar la base de datos con datos de prueba realistas."""
import os
import sys
import django
from datetime import date, timedelta
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.contrib.auth.models import User, Group
from workspace.models import (
    Contratista, Supervisor, Rol, Contrato,
    Adicion, Prorroga, Modificacion, Aclaracion, Suspension, Reinicio, Ampliacion
)

print("Creando usuarios...")

# Superusuario admin
if not User.objects.filter(username='admin').exists():
    admin = User.objects.create_superuser('admin', 'admin@unillanos.edu.co', 'admin1234')
    admin.first_name = 'Administrador'
    admin.last_name = 'Sistema'
    admin.save()
else:
    admin = User.objects.get(username='admin')

# Usuarios con roles
usuarios_data = [
    ('jmendoza', 'Jorge', 'Mendoza Ríos', 'jmendoza@unillanos.edu.co', 'gestor'),
    ('lgarcia', 'Laura', 'García Pérez', 'lgarcia@unillanos.edu.co', 'abogado'),
    ('crodriguez', 'Carlos', 'Rodríguez Silva', 'crodriguez@unillanos.edu.co', 'revisor'),
    ('aperez', 'Ana', 'Pérez López', 'aperez@unillanos.edu.co', 'gestor'),
    ('mlopez', 'Miguel', 'López Martínez', 'mlopez@unillanos.edu.co', 'abogado'),
]

usuarios = {}
for username, first, last, email, rol_tipo in usuarios_data:
    if not User.objects.filter(username=username).exists():
        u = User.objects.create_user(username, email, 'password123')
        u.first_name = first
        u.last_name = last
        u.is_staff = True
        u.save()
    else:
        u = User.objects.get(username=username)
    usuarios[username] = (u, rol_tipo)
    if not Rol.objects.filter(usuario=u, rol=rol_tipo).exists():
        Rol.objects.create(usuario=u, rol=rol_tipo)

print("Creando contratistas...")

contratistas_data = [
    ('Constructora Llanos S.A.S.', 900123456, 'Roberto Herrera', 900123457, '3101234567', 'contacto@llanos.com', None, None),
    ('Servicios Tecnológicos del Meta Ltda.', 901234567, 'Sandra Morales', 901234568, '3209876543', 'admin@sertecmeta.co', None, None),
    ('Consorcio Vías Orientales', 830456789, None, None, '6086512345', 'consorcio@viasorientales.com', None, 'Consorcio Vías Orientales 2024'),
    ('Universidad Nacional de Colombia', 899999034, 'Juan Esteban Morales', 11234567, '6014025555', 'contratos@unal.edu.co', None, None),
    ('Clínica del Meta S.A.', 800345678, 'Patricia Roa', 52987654, '6086523456', 'contratos@clinicameta.co', None, None),
    ('Papelería y Suministros Orinoquia', 900765432, 'Humberto Díaz', 17654321, '3154567890', 'suministros@orinoquia.co', None, None),
    ('Seguridad Privada Llanos Vivos Ltda.', 901876543, 'Gloria Espinosa', 28765432, '3178901234', 'operaciones@llanosvivos.co', None, None),
    ('Constructora Horizonte Verde S.A.S.', 900987654, 'Andrés Camargo', 79876543, '3122345678', 'obras@horizonteverde.co', None, None),
]

contratistas = []
for data in contratistas_data:
    nombre, nit, rep, nit_rep, tel, email, email2, consorcio = data
    c, _ = Contratista.objects.get_or_create(
        nombre=nombre,
        defaults={
            'nit_o_cc': nit,
            'representante_legal': rep,
            'nit_o_cc_representante_legal': nit_rep,
            'telefono': tel,
            'email': email,
            'email_secundario': email2,
            'consorcio': consorcio,
        }
    )
    contratistas.append(c)

print("Creando supervisores...")

supervisores_data = [
    ('Ing. Ramiro Vásquez Castillo', 11223344, 'Jefe de Planta Física', '3141234567', 'rvasquez@unillanos.edu.co'),
    ('Dra. Esperanza Ruiz Mora', 52334455, 'Directora Financiera', '3167654321', 'eruiz@unillanos.edu.co'),
    ('Lic. Fernando Acosta León', 17445566, 'Coordinador Académico', '3191234560', 'facosta@unillanos.edu.co'),
    ('Ing. Valentina Prado Gil', 40556677, 'Jefa de Sistemas', '3205678901', 'vprado@unillanos.edu.co'),
    ('Dr. Gustavo Morales Fuentes', 80667788, 'Rector', '3122223333', 'gmorales@unillanos.edu.co'),
]

supervisores = []
for nombre, nit, cargo, tel, email in supervisores_data:
    s, _ = Supervisor.objects.get_or_create(
        nombre=nombre,
        defaults={
            'nit_o_cc': nit,
            'cargo': cargo,
            'telefono': tel,
            'email': email,
            'fecha_agregado': date(2024, 1, 15),
        }
    )
    supervisores.append(s)

print("Creando contratos...")

hoy = date.today()
gestor = usuarios['jmendoza'][0]
gestor2 = usuarios['aperez'][0]
abogado = usuarios['lgarcia'][0]
abogado2 = usuarios['mlopez'][0]
revisor = usuarios['crodriguez'][0]

contratos_data = [
    # (numero, objeto, tipo, clase, valor, estado, fecha_suscripcion, plazo_inicio, plazo_fin, contratista_idx, supervisor_idx, cdp, rp, fuente)
    (101, 'Suministro de equipos de cómputo y periféricos para las dependencias de la Universidad de los Llanos vigencia 2025', 'Publica', 'Compraventa', 185000000, 'Activo', date(2025, 1, 10), date(2025, 1, 15), date(2025, 12, 31), 1, 3, 1001, 2001, 'Recursos propios'),
    (102, 'Prestación de servicios profesionales para el mantenimiento del sistema de información académica UNILLANOS', 'Directa', 'Prestación de Servicios Profesionales', 48000000, 'Activo', date(2025, 2, 1), date(2025, 2, 5), hoy + timedelta(days=90), 1, 3, 1002, 2002, 'Recursos propios'),
    (103, 'Mantenimiento y adecuación de la planta física del bloque B del campus Barcelona', 'Publica', 'Obra Pública', 320000000, 'Activo', date(2025, 3, 1), date(2025, 3, 10), hoy + timedelta(days=45), 7, 0, 1003, 2003, 'Presupuesto de entidad nacional'),
    (104, 'Suministro de materiales de papelería, útiles de oficina e insumos para la vigencia 2025', 'Directa', 'Suministro', 22500000, 'Activo', date(2025, 1, 20), date(2025, 1, 25), hoy + timedelta(days=120), 5, 1, 1004, 2004, 'Recursos propios'),
    (105, 'Consultoría para la implementación del sistema de gestión de la calidad ISO 9001:2015', 'Privada', 'Consultoría', 95000000, 'Activo', date(2025, 2, 15), date(2025, 3, 1), hoy + timedelta(days=200), 1, 2, 1005, 2005, 'Recursos propios'),
    (106, 'Arrendamiento de vehículos para el transporte de personal académico y administrativo', 'Directa', 'Arrendamiento', 36000000, 'Suspendido', date(2024, 12, 1), date(2024, 12, 5), hoy + timedelta(days=30), 4, 4, 1006, 2006, 'Recursos propios'),
    (107, 'Interadministrativo con la Gobernación del Meta para el desarrollo de programas de extensión universitaria', 'Directa', 'Interadministrativo', 250000000, 'Activo', date(2025, 1, 30), date(2025, 2, 10), hoy + timedelta(days=300), 3, 4, 1007, 2007, 'Presupuesto de entidad nacional'),
    (108, 'Prestación de servicios de seguridad y vigilancia en las instalaciones universitarias', 'Publica', 'Prestación de Servicios', 145000000, 'Activo', date(2025, 1, 5), date(2025, 1, 10), hoy + timedelta(days=60), 6, 0, 1008, 2008, 'Recursos propios'),
    (109, 'Seguro de vida colectivo para docentes y personal administrativo de planta', 'Privada', 'Seguros', 18750000, 'Activo', date(2025, 1, 2), date(2025, 1, 2), date(2025, 12, 31), 4, 1, 1009, 2009, 'Recursos propios'),
    (110, 'Adquisición de libros, bases de datos y recursos bibliográficos digitales para la biblioteca central', 'Publica', 'Compraventa', 67500000, 'Liquidado', date(2024, 6, 1), date(2024, 6, 15), date(2024, 12, 31), 3, 2, 1010, 2010, 'Recursos propios'),
    (111, 'Mantenimiento de redes eléctricas, hidráulicas y de datos del campus principal', 'Directa', 'Prestación de Servicios', 89000000, 'Activo', date(2025, 2, 20), date(2025, 3, 1), hoy + timedelta(days=150), 7, 0, 1011, 2011, 'Recursos propios'),
    (112, 'Cesión de derechos patrimoniales sobre software académico desarrollado por investigadores', 'Directa', 'Cesión Derechos Patrimoniales', 15000000, 'Activo', date(2025, 3, 5), date(2025, 3, 10), hoy + timedelta(days=365), 1, 3, 1012, 2012, 'Recursos propios'),
    (113, 'Suministro de reactivos y materiales de laboratorio para las facultades de ciencias básicas', 'Publica', 'Suministro', 112000000, 'Activo', date(2025, 1, 15), date(2025, 1, 20), hoy + timedelta(days=75), 0, 2, 1013, 2013, 'Regalías'),
    (114, 'Obra pública: Construcción de nuevas aulas y espacios académicos en el campus San Antonio', 'Publica', 'Obra Pública', 850000000, 'Activo', date(2025, 2, 1), date(2025, 2, 28), hoy + timedelta(days=365), 2, 0, 1014, 2014, 'Regalías'),
    (115, 'Prestación de servicios para el diseño e implementación de estrategias de bienestar universitario', 'Directa', 'Prestación de Servicios Profesionales', 28000000, 'Liquidado', date(2024, 8, 1), date(2024, 8, 15), date(2024, 12, 15), 0, 1, 1015, 2015, 'Recursos propios'),
]

contratos = []
for i, data in enumerate(contratos_data):
    num, objeto, tipo, clase, valor, estado, fecha_susc, plazo_ini, plazo_fin, cont_i, sup_i, cdp, rp, fuente = data

    if Contrato.objects.filter(numero_contrato=num).exists():
        c = Contrato.objects.get(numero_contrato=num)
        contratos.append(c)
        continue

    gestor_asig = gestor if i % 2 == 0 else gestor2
    abogado_asig = abogado if i % 2 == 0 else abogado2

    c = Contrato.objects.create(
        numero_contrato=num,
        objeto=objeto,
        tipo_contratacion=tipo,
        clase=clase,
        valor=valor,
        plazo='12 meses' if (plazo_fin - plazo_ini).days > 180 else '6 meses',
        fecha_suscripcion_contrato=fecha_susc,
        plazo_inicio=plazo_ini,
        plazo_fin=plazo_fin,
        estado_contrato=estado,
        contratista=contratistas[cont_i],
        supervisor=supervisores[sup_i],
        gestor=gestor_asig,
        abogado=abogado_asig,
        revisor=revisor,
        CDP_num=cdp + i,
        CDP_fecha=fecha_susc - timedelta(days=5),
        RP_num=rp + i,
        RP_fecha=fecha_susc - timedelta(days=2),
        rubro_presupuestal=f'2-3-{1000+i}-001' if fuente == 'Recursos propios' else f'5-1-{2000+i}-001',
        fuente_recursos=fuente,
        numero_poliza=500000 + i if clase != 'Interadministrativo' else 0,
        fecha_poliza_expedicion=fecha_susc,
        fecha_poliza_aprobacion=fecha_susc + timedelta(days=3),
        aseguradora='Mapfre Seguros' if i % 2 == 0 else 'Seguros Bolívar',
        dependencia_responsable=['Rectoría', 'Vicerrectoría Académica', 'Vicerrectoría Administrativa', 'Planta Física', 'Sistemas'][i % 5],
        ubicacion='Villavicencio, Meta',
        presupuesto_programado=valor * 1.05,
        modalidad_seleccion=tipo,
        almacen=clase in ('Compraventa', 'Suministro'),
        fecha_liquidacion=date(2025, 1, 20) if estado == 'Liquidado' else None,
        publicacion_secop='https://www.secop.gov.co',
        fecha_publicacion_secop=fecha_susc + timedelta(days=1) if estado != 'Sin Clasificar' else None,
    )
    contratos.append(c)

print("Creando modificaciones a contratos...")

# Adición al contrato 103 (obra pública)
if contratos[2] and not contratos[2].adiciones.exists():
    Adicion.objects.create(
        contrato=contratos[2],
        adicion_1='Adición de recursos para imprevistos en obra',
        valor_total=45000000,
        fecha=date(2025, 4, 1),
    )

# Prórroga al contrato 106 (suspendido)
if contratos[5] and not contratos[5].prorrogas.exists():
    Prorroga.objects.create(
        contrato=contratos[5],
        fecha=date(2025, 1, 15),
        justificacion='El contratista solicitó prórroga por situaciones de fuerza mayor relacionadas con el orden público regional.',
        nueva_fecha_terminacion=hoy + timedelta(days=60),
    )

# Suspensión al contrato 106
if contratos[5] and not contratos[5].suspensiones.exists():
    Suspension.objects.create(
        contrato=contratos[5],
        fecha_subscripcion=date(2025, 2, 1),
        plazo=date(2025, 4, 30),
        fecha_posible_reinicio=date(2025, 5, 1),
    )

# Modificación al contrato 107
if contratos[6] and not contratos[6].modificaciones.exists():
    Modificacion.objects.create(
        contrato=contratos[6],
        fecha_subscripcion=date(2025, 3, 15),
        motivo='Ajuste de actividades según cronograma aprobado por la Gobernación del Meta.',
    )

# Aclaración al contrato 101
if contratos[0] and not contratos[0].aclaraciones.exists():
    Aclaracion.objects.create(
        contrato=contratos[0],
        fecha_subscripcion=date(2025, 2, 10),
        motivo='Aclaración de especificaciones técnicas para monitores y teclados incluidos en el objeto contractual.',
    )

print("\n✓ Datos creados exitosamente.")
print("\nCredenciales:")
print("  Admin (superusuario): admin / admin1234")
print("  Gestor:   jmendoza / password123")
print("  Abogado:  lgarcia  / password123")
print("  Revisor:  crodriguez / password123")
print(f"\nContratos creados: {Contrato.objects.count()}")
print(f"Contratistas: {Contratista.objects.count()}")
print(f"Supervisores: {Supervisor.objects.count()}")
print(f"Usuarios: {User.objects.count()}")
