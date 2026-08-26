try {
    // 1. Limpeza (Cleanup) do Permission Set antigo
    List<PermissionSet> existing = [SELECT Id FROM PermissionSet WHERE Name = 'Agentforce_CRM_Access'];
    if (!existing.isEmpty()) {
        delete existing;
        System.debug('🧹 SUCESSO: Permission Set antigo removido.');
    }

    // 2. Busca o Usuário do Bot e a Classe Apex
    User botUser = [SELECT Id, Name FROM User WHERE Username LIKE 'acme_investment_banker_assistant%' LIMIT 1];
    ApexClass resolverClass = [SELECT Id FROM ApexClass WHERE Name = 'ACME_ScopeResolverAction' LIMIT 1];

    // 3. Cria o novo Permission Set
    PermissionSet ps = new PermissionSet(Name = 'Agentforce_CRM_Access', Label = 'Agentforce CRM Access');
    insert ps;

    // 4. Permissões de Objeto (CRM)
    insert new ObjectPermissions(ParentId = ps.Id, SobjectType = 'Account', PermissionsRead = true);
    insert new ObjectPermissions(ParentId = ps.Id, SobjectType = 'Opportunity', PermissionsRead = true);

    // 5. Permissão Crítica: Acesso de execução à Classe Apex
    insert new SetupEntityAccess(ParentId = ps.Id, SetupEntityId = resolverClass.Id);

    // 6. Atribuição ao Bot
    insert new PermissionSetAssignment(AssigneeId = botUser.Id, PermissionSetId = ps.Id);

    System.debug('✅ SUCESSO ABSOLUTO: Permissoes de CRM e Apex concedidas ao Bot: ' + botUser.Name);
} catch (Exception e) {
    System.debug('❌ ERRO FATAL: ' + e.getMessage());
}
