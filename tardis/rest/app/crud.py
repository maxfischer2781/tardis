async def get_resource_state(sql_registry, drone_uuid: str):
    sql_query = """
    SELECT R.drone_uuid, RS.state
    FROM Resources R
    JOIN ResourceStates RS ON R.state_id = RS.state_id
    WHERE R.drone_uuid = :drone_uuid"""
    return await sql_registry.async_execute(sql_query, dict(drone_uuid=drone_uuid))


async def get_resources(sql_registry):
    sql_query = """
    SELECT R.remote_resource_uuid , RS.state, R.drone_uuid, S.site_name,
    MT.machine_type, R.created, R.updated
    FROM Resources R
    JOIN ResourceStates RS ON R.state_id = RS.state_id
    JOIN Sites S ON R.site_id = S.site_id
    JOIN MachineTypes MT ON R.machine_type_id = MT.machine_type_id"""
    return await sql_registry.async_execute(sql_query, {})
