try {
    // 1. Reutiliza o Permission Set existente (NAO deletar - esta em uso)
    PermissionSet ps = [SELECT Id FROM PermissionSet WHERE Name = 'Agentforce_CRM_Access' LIMIT 1];

    // 2. Busca a Classe Apex do Scope Resolver
    ApexClass resolverClass = [SELECT Id, Name FROM ApexClass WHERE Name = 'ACME_ScopeResolverAction' LIMIT 1];

    // 3. Verifica se o acesso a classe ja existe, evitando duplicidade
    List<SetupEntityAccess> existingAccess = [
        SELECT Id FROM SetupEntityAccess
        WHERE ParentId = :ps.Id AND SetupEntityId = :resolverClass.Id
    ];

    if (existingAccess.isEmpty()) {
        insert new SetupEntityAccess(ParentId = ps.Id, SetupEntityId = resolverClass.Id);
        System.debug('SUCESSO: Acesso a classe Apex ' + resolverClass.Name + ' concedido ao Permission Set.');
    } else {
        System.debug('AVISO: Acesso a classe Apex ja existia. Nenhuma alteracao necessaria.');
    }

    // 4. Confirma que o bot ja possui o Permission Set atribuido
    User botUser = [SELECT Id, Name FROM User WHERE Username LIKE 'acme_investment_banker_assistant%' LIMIT 1];
    List<PermissionSetAssignment> assign = [
        SELECT Id FROM PermissionSetAssignment
        WHERE AssigneeId = :botUser.Id AND PermissionSetId = :ps.Id
    ];
    System.debug(assign.isEmpty()
        ? 'ATENCAO: Bot ainda NAO possui o Permission Set atribuido!'
        : 'CONFIRMADO: Bot ja possui o Permission Set atribuido.');

    System.debug('SUCESSO ABSOLUTO: Permission Set ' + ps.Id + ' atualizado com acesso Apex.');
} catch (Exception e) {
    System.debug('ERRO FATAL: ' + e.getMessage());
}
