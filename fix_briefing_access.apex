try {
    PermissionSet ps = [SELECT Id FROM PermissionSet WHERE Name = 'Agentforce_CRM_Access' LIMIT 1];
    ApexClass briefingClass = [SELECT Id, Name FROM ApexClass WHERE Name LIKE '%Briefing%' LIMIT 1];

    List<SetupEntityAccess> existingAccess = [
        SELECT Id FROM SetupEntityAccess
        WHERE ParentId = :ps.Id AND SetupEntityId = :briefingClass.Id
    ];

    if (existingAccess.isEmpty()) {
        insert new SetupEntityAccess(ParentId = ps.Id, SetupEntityId = briefingClass.Id);
        System.debug('SUCESSO: Acesso a classe ' + briefingClass.Name + ' concedido ao Permission Set.');
    } else {
        System.debug('AVISO: Acesso ja existia.');
    }
} catch (Exception e) {
    System.debug('ERRO FATAL: ' + e.getMessage());
}
