from abc import ABC

class LTLFormula(ABC):
    pass

class PropositionLTLFormula(LTLFormula):
    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def propositions(*args) -> list["PropositionLTLFormula"]:
        assert len(args) > 0 and all(isinstance(arg, str) for arg in args), "Only non-empty list of strings is allowed. "
        return [PropositionLTLFormula(name) for name in args]

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class InfinitePath:
    def __init__(self, linear_path: list[set[PropositionLTLFormula]], lasso_start_index: int):
        assert 0 <= lasso_start_index < len(linear_path), "lasso must start at some point of the linear path."
        pass

    def satisfies(self, formula: LTLFormula):
        pass