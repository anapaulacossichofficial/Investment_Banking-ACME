public with sharing class ACME_ScopeResolverAction {
    
    public class ResolverInput {
        @InvocableVariable(required=true description='The name of the Account requested by the user (e.g., GLOBALTRUST CAPITAL)')
        public String accountName;
    }

    public class ResolverOutput {
        @InvocableVariable(description='The 18-character Salesforce ID of the Account')
        public String accountId;
        
        @InvocableVariable(description='Status of the resolution: locked, not_found, or error')
        public String scopeStatus;
    }

    @InvocableMethod(label='ACME Scope Resolver' description='Searches for an Account by name and returns its ID for Meeting Prep grounding.')
    public static List<ResolverOutput> resolveScope(List<ResolverInput> inputs) {
        List<ResolverOutput> results = new List<ResolverOutput>();

        for (ResolverInput input : inputs) {
            ResolverOutput output = new ResolverOutput();
            try {
                String searchTerm = '%' + input.accountName.trim() + '%';
                // Atualizado para a API 67.0: uso de WITH USER_MODE em vez de SECURITY_ENFORCED
                List<Account> accounts = [SELECT Id, Name FROM Account WHERE Name LIKE :searchTerm WITH USER_MODE LIMIT 1];

                if (!accounts.isEmpty()) {
                    output.accountId = accounts[0].Id;
                    output.scopeStatus = 'locked';
                } else {
                    output.accountId = null;
                    output.scopeStatus = 'not_found';
                }
            } catch (Exception e) {
                output.accountId = null;
                output.scopeStatus = 'error: ' + e.getMessage();
            }
            results.add(output);
        }
        return results;
    }
}
