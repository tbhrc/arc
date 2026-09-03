# Configuration Contract

ARC configuration is non-secret deployment intent.

The JSON profile defines:

- ARC contract version;
- target GitHub owner/type;
- default repository visibility;
- core repositories and roles;
- business domain repositories;
- declared integration categories.

Rules:

1. No credential values.
2. Existing repositories may be reused.
3. Repository names are deployment choices, not architecture truth.
4. A profile can be committed only when it contains no sensitive business-specific data.
5. Provider-specific IDs should be added only when safe and useful; secret values remain outside the profile.
