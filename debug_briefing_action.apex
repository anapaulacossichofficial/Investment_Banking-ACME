try {
    Id targetAccountId = '001aj00003M2aN4AAJ';

    Account acc = [
        SELECT Id, Name, Industry, Type, AnnualRevenue, Rating, OwnerId, Owner.Name
        FROM Account WHERE Id = :targetAccountId LIMIT 1
    ];
    System.debug('CONFIRMADO: Account existe e e visivel via SOQL padrao -> ' + acc.Name);

    System.debug('Formato do Id recebido: ' + String.valueOf(targetAccountId).length() + ' caracteres');

    ApexClass briefingClass = [SELECT Id, Name FROM ApexClass WHERE Name LIKE '%Briefing%' LIMIT 1];
    System.debug('Classe Apex da Action Meeting_Prep_Briefing encontrada: ' + briefingClass.Name);

    PermissionSet ps = [SELECT Id FROM PermissionSet WHERE Name = 'Agentforce_CRM_Access' LIMIT 1];
    List<SetupEntityAccess> briefingAccess = [
        SELECT Id FROM SetupEntityAccess
        WHERE ParentId = :ps.Id AND SetupEntityId = :briefingClass.Id
    ];
    System.debug(briefingAccess.isEmpty()
        ? 'ATENCAO: Permission Set NAO tem acesso a classe da Action de Briefing!'
        : 'CONFIRMADO: Permission Set ja tem acesso a classe da Action de Briefing.');

} catch (Exception e) {
    System.debug('ERRO: ' + e.getMessage());
}
