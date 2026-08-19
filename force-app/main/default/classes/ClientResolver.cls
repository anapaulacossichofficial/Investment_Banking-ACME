public with sharing class ClientResolver {
    public static List<Account> resolveByName(String accountName) {
        if (String.isBlank(accountName)) {
            return new List<Account>();
        }
        return [
            SELECT Id, Name, BillingCity, BillingState, BillingCountry
            FROM Account
            WHERE Name = :accountName
            WITH SECURITY_ENFORCED
            LIMIT 5
        ];
    }
}
