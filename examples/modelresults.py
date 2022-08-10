from sampler import *


class ModelResult(Sampler):
    _country = ListField(["SE", "US", "DE"])
    locale = MapField("_country", {"SE": "se_SE", "US": "en_US", "DE": "de_DE"})

    orderId = IncrementField()
    decision = ListField(["ACCEPT", "REJECT"])
    decisionTime = Field(var="ts")
    requestTime = Field(var="ts")
    rejectReason = WeightedListField(
        [
            ("foo", 0.8),
            ("bar", 0.15),
            ("zzz", 0.05),
        ]
    )

    variableVector = Sampler(BRMS=Sampler(foo=Field("a")))


generator = ModelResult(decisionTime=123)

print(generator.generate())
