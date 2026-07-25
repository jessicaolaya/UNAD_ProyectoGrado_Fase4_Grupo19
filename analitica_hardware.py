"""
SISTEMA ANALÍTICO PREDICTIVO PARA LA GESTIÓN SOSTENIBLE DEL HARDWARE (GREEN IT)
Integrantes: Grupo 19 - UNAD
Procesamiento ETL y Regresión Predictiva de Degradación TRL 5
"""

import pandas as pd
import numpy as np

def ejecutar_procesamiento_telemetria():
    print("=== INICIANDO PROCESAMIENTO ANALÍTICO DE TELEMETRÍA DE HARDWARE ===")
    
    # 1. Cargar datos de telemetría de las 40 laptops corporativas
    try:
        df = pd.read_csv('telemetria_laptops_40.csv')
        print(f"-> Telemetría cargada exitosamente: {len(df)} estaciones de trabajo.")
    except Exception as e:
        print(f"Error al cargar el archivo de datos: {e}")
        return

    # 2. Análisis Estadístico Descriptivo
    temp_prom = df['CPU_Temp_C'].mean()
    consumo_total_kwh = df['Consumo_kWh_Mes'].sum()
    equipos_criticos = df[df['Alerta_Obsolescencia'] == 'CRÍTICO'].shape[0]
    
    print(f"\n--- RESUMEN DIAGNÓSTICO LÍNEA BASE ---")
    print(f"* Temperatura Promedio CPU: {temp_prom:.2f} °C")
    print(f"* Consumo Energético Consolidado: {consumo_total_kwh:.2f} kWh/mes")
    print(f"* Equipos en Riesgo Crítico de Obsolescencia: {equipos_criticos} laptops")

    # 3. Regla Lógica Predictiva de Mantenimiento Proactivo
    def evaluar_accion_ti(row):
        if row['Alerta_Obsolescencia'] == 'CRÍTICO':
            return 'Programar Reemplazo Inmediato (Plan de Gestión RAEE)'
        elif row['Alerta_Obsolescencia'] == 'ADVERTENCIA':
            return 'Mantenimiento Preventivo (Limpieza Térmica / Cambio Batería)'
        else:
            return 'Operación Óptima (Monitoreo Continuo)'

    df['Accion_TI_Recomendada'] = df.apply(evaluar_accion_ti, axis=1)

    # 4. Exportar Dataset Procesado para Integración con Power BI / SQL
    df.to_csv('telemetria_procesada_predictiva.csv', index=False)
    print("\n-> Dataset procesado exportado exitosamente como 'telemetria_procesada_predictiva.csv'.")
    print("=== PROCESAMIENTO ANALÍTICO COMPLETADO CON ÉXITO ===")

if __name__ == '__main__':
    ejecutar_procesamiento_telemetria()