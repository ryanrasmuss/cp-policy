# cp-policy.py

Install policy script for Check Point (outdated by R81)

Add Policy names to ``config.txt`` and specify gateways to install policy on in the same line seperated by a comma. You do not need to specify gateways if the policy package already has specified gateways defined in the settings.

```
#Policy,gateway1,gateway2
Policy1,gateway-1,gateway2
Policy2
Policy3,gateway-3
```

Policy 2 will be installed on all gateways or the gateways specified in the policy package.
Policy 1 will be installed on gateways: gateway1, gateway2
Policy 3 will be install on gateway-3
