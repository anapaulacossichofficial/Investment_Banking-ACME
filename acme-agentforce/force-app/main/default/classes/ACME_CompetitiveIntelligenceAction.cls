public class ACME_CompetitiveIntelligenceAction {

    public class Request {
        @InvocableVariable(required=true label='Company Name or Ticker')
        public String query;
    }

    public class Response {
        @InvocableVariable(label='Competitive Intelligence Result')
        public String result;
    }

    @InvocableMethod(label='Get Competitive Intelligence' description='Fetches competitive intelligence data from ACME external API')
    public static List<Response> getIntelligence(List<Request> requests) {
        List<Response> responses = new List<Response>();

        for (Request req : requests) {
            Response res = new Response();
            try {
                HttpRequest httpReq = new HttpRequest();
                httpReq.setEndpoint('callout:ACME_Competitive_Intelligence/competitive-intelligence?query=' + EncodingUtil.urlEncode(req.query, 'UTF-8'));
                httpReq.setMethod('GET');
                httpReq.setTimeout(20000);

                Http http = new Http();
                HttpResponse httpRes = http.send(httpReq);

                if (httpRes.getStatusCode() == 200) {
                    res.result = httpRes.getBody();
                } else {
                    res.result = 'Error: HTTP ' + httpRes.getStatusCode() + ' - ' + httpRes.getBody();
                }
            } catch (Exception e) {
                res.result = 'Error calling external service: ' + e.getMessage();
            }
            responses.add(res);
        }

        return responses;
    }
}