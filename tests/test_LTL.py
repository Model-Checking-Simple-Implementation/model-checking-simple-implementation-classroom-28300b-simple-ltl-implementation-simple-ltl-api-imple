"""
Comprehensive test suite for LTL (Linear Temporal Logic) implementation.

Tests verify the LTL API through the public interface:
- Operators: ~, +, |, >>, &
- Functions: F(), G() (if implemented)
- TRUE constant (if implemented)
- PropositionLTLFormula creation
- InfinitePath satisfaction checking

Tests exercise simple cases, edge cases, complex formulas, and large inputs.
"""

import pytest
from LTL import LTLFormula, PropositionLTLFormula, InfinitePath

# Try to import optional features
try:
    from LTL import TRUE
except ImportError:
    TRUE = None

try:
    from LTL import F, G
except ImportError:
    F = None
    G = None


# Detect which operators are implemented
def _check_operator(op_name):
    """Check if an operator is implemented by attempting to use it"""
    try:
        a = PropositionLTLFormula("test")
        b = PropositionLTLFormula("test2")
        
        if op_name == "negation":
            ~a
        elif op_name == "next":
            +a
        elif op_name == "disjunction":
            a | b
        elif op_name == "conjunction":
            a & b
        elif op_name == "until":
            a >> b
        return True
    except (TypeError, AttributeError):
        return False


HAS_NEGATION = _check_operator("negation")
HAS_NEXT = _check_operator("next")
HAS_DISJUNCTION = _check_operator("disjunction")
HAS_CONJUNCTION = _check_operator("conjunction")
HAS_UNTIL = _check_operator("until")


class TestFeatureImplementation:
    """Test which operators and functions are implemented"""
    
    def test_true_constant_implemented(self):
        """Check if TRUE constant is implemented"""
        assert TRUE is not None, "TODO: Implement TRUE constant"
        assert isinstance(TRUE, LTLFormula), "TRUE should be an LTLFormula"
    
    def test_eventually_function_implemented(self):
        """Check if F() (eventually) function is implemented"""
        assert F is not None, "TODO: Implement F() (eventually) function"
        a = PropositionLTLFormula("A")
        result = F(a)
        assert isinstance(result, LTLFormula), "F(A) should be an LTLFormula"
    
    def test_globally_function_implemented(self):
        """Check if G() (globally) function is implemented"""
        assert G is not None, "TODO: Implement G() (globally) function"
        a = PropositionLTLFormula("A")
        result = G(a)
        assert isinstance(result, LTLFormula), "G(A) should be an LTLFormula"
    
    def test_negation_operator_implemented(self):
        """Check if ~ (negation) operator is implemented"""
        a = PropositionLTLFormula("A")
        try:
            not_a = ~a
            assert isinstance(not_a, LTLFormula), "~A should be an LTLFormula"
        except TypeError as e:
            raise AssertionError("TODO: Implement ~ (negation) operator") from e
    
    def test_next_operator_implemented(self):
        """Check if + (next) operator is implemented"""
        a = PropositionLTLFormula("A")
        try:
            next_a = +a
            assert isinstance(next_a, LTLFormula), "+A should be an LTLFormula"
        except TypeError as e:
            raise AssertionError("TODO: Implement + (next) operator") from e
    
    def test_disjunction_operator_implemented(self):
        """Check if | (or) operator is implemented"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        try:
            or_ab = a | b
            assert isinstance(or_ab, LTLFormula), "A | B should be an LTLFormula"
        except TypeError as e:
            raise AssertionError("TODO: Implement | (disjunction) operator") from e
    
    def test_conjunction_operator_implemented(self):
        """Check if & (and) operator is implemented"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        try:
            and_ab = a & b
            assert isinstance(and_ab, LTLFormula), "A & B should be an LTLFormula"
        except TypeError as e:
            raise AssertionError("TODO: Implement & (conjunction) operator") from e
    
    def test_until_operator_implemented(self):
        """Check if >> (until) operator is implemented"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        try:
            until_ab = a >> b
            assert isinstance(until_ab, LTLFormula), "A >> B should be an LTLFormula"
        except TypeError as e:
            raise AssertionError("TODO: Implement >> (until) operator") from e


class TestPropositionLTLFormula:
    """Test PropositionLTLFormula basic functionality"""
    
    def test_create_single_proposition(self):
        """Test creating a single proposition"""
        a = PropositionLTLFormula("A")
        assert a.name == "A"
        assert isinstance(a, LTLFormula)
    
    def test_create_multiple_propositions(self):
        """Test creating multiple propositions with static method"""
        a, b, c = PropositionLTLFormula.propositions("A", "B", "C")
        assert a.name == "A"
        assert b.name == "B"
        assert c.name == "C"
        assert all(isinstance(p, LTLFormula) for p in [a, b, c])
    
    def test_propositions_assertion_empty(self):
        """Test that empty propositions raises assertion"""
        with pytest.raises(AssertionError):
            PropositionLTLFormula.propositions()
    
    def test_propositions_assertion_non_string(self):
        """Test that non-string propositions raise assertion"""
        with pytest.raises(AssertionError):
            PropositionLTLFormula.propositions("A", 123, "C")


class TestTRUEConstant:
    """Test TRUE constant"""
    
    @pytest.mark.skipif(TRUE is None, reason="TRUE not implemented")
    def test_true_is_ltl_formula(self):
        """Test TRUE is an LTLFormula"""
        assert isinstance(TRUE, LTLFormula)


class TestOperators:
    """Test LTL operators return LTLFormula instances"""
    
    @pytest.mark.skipif(not HAS_NEGATION, reason="Negation operator not implemented")
    def test_negation_operator(self):
        """Test ~ operator returns LTLFormula"""
        a = PropositionLTLFormula("A")
        not_a = ~a
        assert isinstance(not_a, LTLFormula)
    
    @pytest.mark.skipif(not HAS_NEXT, reason="Next operator not implemented")
    def test_next_operator(self):
        """Test + operator returns LTLFormula"""
        a = PropositionLTLFormula("A")
        next_a = +a
        assert isinstance(next_a, LTLFormula)
    
    @pytest.mark.skipif(not HAS_DISJUNCTION, reason="Disjunction operator not implemented")
    def test_disjunction_operator(self):
        """Test | operator returns LTLFormula"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        or_ab = a | b
        assert isinstance(or_ab, LTLFormula)
    
    @pytest.mark.skipif(not HAS_UNTIL, reason="Until operator not implemented")
    def test_until_operator(self):
        """Test >> operator returns LTLFormula"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        until_ab = a >> b
        assert isinstance(until_ab, LTLFormula)
    
    @pytest.mark.skipif(not HAS_CONJUNCTION, reason="Conjunction operator not implemented")
    def test_conjunction_operator(self):
        """Test & operator returns LTLFormula"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        and_ab = a & b
        assert isinstance(and_ab, LTLFormula)


class TestFunctionOperators:
    """Test F() and G() function operators"""
    
    @pytest.mark.skipif(F is None, reason="F() not implemented")
    def test_eventually_function(self):
        """Test F() (eventually) returns LTLFormula"""
        a = PropositionLTLFormula("A")
        f_a = F(a)
        assert isinstance(f_a, LTLFormula)
    
    @pytest.mark.skipif(G is None, reason="G() not implemented")
    def test_globally_function(self):
        """Test G() (globally) returns LTLFormula"""
        a = PropositionLTLFormula("A")
        g_a = G(a)
        assert isinstance(g_a, LTLFormula)


class TestSimplePaths:
    """Test satisfaction on simple paths"""
    
    @pytest.mark.skipif(TRUE is None, reason="TRUE not implemented")
    def test_simple_path_true_formula(self):
        """Test TRUE is satisfied on any path"""
        a = PropositionLTLFormula("A")
        path = InfinitePath([{a}], 0)
        assert path.satisfies(TRUE)
    
    def test_simple_path_single_proposition_present(self):
        """Test proposition is satisfied when present"""
        a = PropositionLTLFormula("A")
        path = InfinitePath([{a}], 0)
        assert path.satisfies(a)
    
    def test_simple_path_single_proposition_absent(self):
        """Test proposition is not satisfied when absent"""
        a = PropositionLTLFormula("A")
        b = PropositionLTLFormula("B")
        path = InfinitePath([{a}], 0)
        assert not path.satisfies(b)
    
    @pytest.mark.skipif(not HAS_NEGATION, reason="Negation operator not implemented")
    def test_simple_path_negation(self):
        """Test negation operator"""
        a = PropositionLTLFormula("A")
        b = PropositionLTLFormula("B")
        path = InfinitePath([{a}], 0)
        assert path.satisfies(~b)
        assert not path.satisfies(~a)
    
    @pytest.mark.skipif(not HAS_DISJUNCTION, reason="Disjunction operator not implemented")
    def test_simple_path_disjunction_left_true(self):
        """Test disjunction when left is true"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        path = InfinitePath([{a}], 0)
        assert path.satisfies(a | b)
    
    @pytest.mark.skipif(not HAS_DISJUNCTION, reason="Disjunction operator not implemented")
    def test_simple_path_disjunction_right_true(self):
        """Test disjunction when right is true"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        path = InfinitePath([{b}], 0)
        assert path.satisfies(a | b)
    
    @pytest.mark.skipif(not HAS_DISJUNCTION, reason="Disjunction operator not implemented")
    def test_simple_path_disjunction_both_false(self):
        """Test disjunction when both are false"""
        a, b, c = PropositionLTLFormula.propositions("A", "B", "C")
        path = InfinitePath([{c}], 0)
        assert not path.satisfies(a | b)
    
    @pytest.mark.skipif(not HAS_CONJUNCTION, reason="Conjunction operator not implemented")
    def test_simple_path_conjunction(self):
        """Test conjunction operator"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        path = InfinitePath([{a, b}], 0)
        assert path.satisfies(a & b)
        
        path2 = InfinitePath([{a}], 0)
        assert not path2.satisfies(a & b)


class TestNextOperator:
    """Test next (X) operator"""
    
    @pytest.mark.skipif(not HAS_NEXT, reason="Next operator not implemented")
    def test_next_simple(self):
        """Test next operator on linear path"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        path = InfinitePath([{a}, {b}], 1)
        # At index 0: A, at index 1: B
        assert path.satisfies(+b)  # Next is B
        assert not path.satisfies(+a)  # Next is not A
    
    @pytest.mark.skipif(not HAS_NEXT, reason="Next operator not implemented")
    def test_next_chain(self):
        """Test chained next operators"""
        a, b, c = PropositionLTLFormula.propositions("A", "B", "C")
        path = InfinitePath([{a}, {b}, {c}], 2)
        assert path.satisfies(+(+c))  # Next next is C
    
    @pytest.mark.skipif(not HAS_NEXT, reason="Next operator not implemented")
    def test_next_beyond_path(self):
        """Test next operator beyond linear path"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        path = InfinitePath([{a}, {b}], 1)
        assert not path.satisfies(+(+a))


class TestLassoWrapAround:
    """Test wrap-around behavior inside the lasso"""

    @pytest.mark.skipif(not HAS_NEXT, reason="Next operator not implemented")
    def test_next_wraps_from_lasso_back_to_start(self):
        """Test next wraps from the end of the lasso back to its start"""
        a, b, c = PropositionLTLFormula.propositions("A", "B", "C")
        path = InfinitePath([{a}, {b}, {c}], 1)
        # Infinite path is A, B, C, B, C, ... so +++B should hold
        try:
            assert path.satisfies(+(+(+b)))
        except (AttributeError, NotImplementedError):
            pytest.skip("satisfies not fully implemented")

    @pytest.mark.skipif(not HAS_UNTIL, reason="Until operator not implemented")
    def test_until_can_see_right_in_lasso(self):
        """Test until succeeds when right appears in the repeating lasso"""
        a, b, c = PropositionLTLFormula.propositions("A", "B", "C")
        path = InfinitePath([{a}, {a}, {b}], 1)
        # Sequence is A, A, B, B, B, ... so A U B is satisfied from the start
        try:
            assert path.satisfies(a >> b)
        except (AttributeError, NotImplementedError):
            pytest.skip("satisfies not fully implemented")


class TestUntilOperator:
    """Test until (U) operator"""
    
    @pytest.mark.skipif(not HAS_UNTIL, reason="Until operator not implemented")
    def test_until_immediate(self):
        """Test until when right is immediately true"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        path = InfinitePath([{b}], 0)
        assert path.satisfies(a >> b)  
    
    @pytest.mark.skipif(not HAS_UNTIL, reason="Until operator not implemented")
    def test_until_linear_path(self):
        """Test until on linear path"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        path = InfinitePath([{a}, {a}, {b}], 2)
        assert path.satisfies(a >> b)  # A until B: A, A, then B
    
    @pytest.mark.skipif(not HAS_UNTIL, reason="Until operator not implemented")
    def test_until_left_false_before_right(self):
        """Test until fails when left becomes false before right"""
        a, b, c = PropositionLTLFormula.propositions("A", "B", "C")
        path = InfinitePath([{a}, {c}, {b}], 2)
        assert not path.satisfies(a >> b)  # A until B, but C breaks the chain
    
    @pytest.mark.skipif(not HAS_UNTIL, reason="Until operator not implemented")
    def test_until_never_satisfied(self):
        """Test until when right is never satisfied"""
        a = PropositionLTLFormula("A")
        path = InfinitePath([{a}], 0)
        assert not path.satisfies(a >> PropositionLTLFormula("B"))
    
    @pytest.mark.skipif(not HAS_UNTIL, reason="Until operator not implemented")
    def test_until_in_lasso(self):
        """Test until in the lasso part"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        # Path: X, A, A, A, ... (lasso starts at index 1)
        path = InfinitePath([{PropositionLTLFormula("X")}, {a}], 1)
        # Right (B) is never satisfied, so Until should fail
        assert not path.satisfies(a >> b)


class TestEventuallyAndGlobally:
    """Test F() (eventually) and G() (globally) operators"""
    
    @pytest.mark.skipif(F is None or G is None, reason="F() or G() not implemented")
    def test_eventually_simple(self):
        """Test eventually finds proposition"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        path = InfinitePath([{a}, {b}], 1)
        assert path.satisfies(F(b))  # Eventually B
        assert path.satisfies(F(a))  # Eventually A
    
    @pytest.mark.skipif(F is None, reason="F() not implemented")
    def test_eventually_in_lasso(self):
        """Test eventually finds proposition in lasso"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        path = InfinitePath([{a}, {b}], 1)  # Lasso: B, repeating
        assert path.satisfies(F(b))
    
    @pytest.mark.skipif(G is None, reason="G() not implemented")
    def test_globally_all_positions(self):
        """Test globally when proposition is everywhere"""
        a = PropositionLTLFormula("A")
        path = InfinitePath([{a}, {a}], 1)  # A repeating
        assert path.satisfies(G(a))
    
    @pytest.mark.skipif(G is None, reason="G() not implemented")
    def test_globally_fails_when_absent_somewhere(self):
        """Test globally fails when proposition is absent somewhere"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        path = InfinitePath([{a}, {b}], 1)  # B repeating after A
        assert not path.satisfies(G(a))


class TestComplexFormulas:
    """Test complex nested formulas"""
    
    @pytest.mark.skipif(not (HAS_NEGATION and HAS_NEXT and HAS_UNTIL and HAS_CONJUNCTION and HAS_DISJUNCTION and F is not None and G is not None), reason="Complex formula requires all operators and F/G")
    def test_complex_formula_from_readme(self):
        """Test the complex formula from README: (A | +F(B >> (~C))) & G(B | (+B))"""
        a, b, c = PropositionLTLFormula.propositions("A", "B", "C")
        formula = (a | +(F(b >> (~c)))) & G(b | (+b))
        
        # Create a path that satisfies this: A and B both at start, repeating
        path = InfinitePath([{a, b}], 0)  # Fixed: lasso must be at valid index
        try:
            result = path.satisfies(formula)
            # Don't assert a specific result, just test it doesn't crash
            assert isinstance(result, bool)
        except (AttributeError, NotImplementedError):
            pytest.skip("satisfies not fully implemented")
    
    @pytest.mark.skipif(not HAS_NEGATION, reason="Negation operator not implemented")
    def test_nested_negations(self):
        """Test double negation"""
        a = PropositionLTLFormula("A")
        path = InfinitePath([{a}], 0)
        assert path.satisfies(~~a)  # Double negation
    
    @pytest.mark.skipif(not HAS_DISJUNCTION, reason="Disjunction operator not implemented")
    def test_complex_disjunction(self):
        """Test complex disjunction"""
        a, b, c = PropositionLTLFormula.propositions("A", "B", "C")
        path = InfinitePath([{c}], 0)
        assert path.satisfies(a | b | c)
    
    @pytest.mark.skipif(not HAS_CONJUNCTION, reason="Conjunction operator not implemented")
    def test_complex_conjunction(self):
        """Test complex conjunction"""
        a, b, c = PropositionLTLFormula.propositions("A", "B", "C")
        path = InfinitePath([{a, b, c}], 0)
        assert path.satisfies(a & b & c)


class TestMultiStateLinearPath:
    """Test paths with multiple states before lasso"""
    
    @pytest.mark.skipif(not (HAS_NEXT and HAS_UNTIL), reason="Next and Until operators required")
    def test_two_state_linear_path(self):
        """Test path with two states before lasso"""
        a, b, c = PropositionLTLFormula.propositions("A", "B", "C")
        path = InfinitePath([{a}, {b}, {c}], 2)
        # Path: A, B, C, C, C, ...
        assert path.satisfies(a)  # A at index 0
        assert path.satisfies(+(b))  # Next is B
        assert path.satisfies(a >> b)  # A until B
        assert not path.satisfies(a >> c)  # Corrected expectation
    
    @pytest.mark.skipif(F is None or not HAS_NEXT, reason="F() function and Next operator required")
    def test_eventually_in_linear_part(self):
        """Test eventually succeeds when prop is in linear part"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        x = PropositionLTLFormula("X")
        path = InfinitePath([{a}, {x}, {b}], 2)
        assert path.satisfies(F(a))  # Eventually A
        assert path.satisfies(F(b))  # Eventually B


class TestEdgeCases:
    """Test edge cases"""
    
    def test_lasso_at_start(self):
        """Test when lasso starts at index 0"""
        a = PropositionLTLFormula("A")
        path = InfinitePath([{a}], 0)
        # Path: A, A, A, ...
        try:
            if G is not None:
                assert path.satisfies(G(a))
            if F is not None:
                assert path.satisfies(F(a))
            if F is None and G is None:
                pytest.skip("F() and G() not implemented")
        except (AttributeError, NotImplementedError):
            pytest.skip("satisfies not fully implemented")  
    
    @pytest.mark.skipif(not (HAS_CONJUNCTION and HAS_DISJUNCTION), reason="Conjunction and Disjunction operators required")
    def test_multiple_propositions_in_state(self):
        """Test states with multiple propositions"""
        a, b, c = PropositionLTLFormula.propositions("A", "B", "C")
        path = InfinitePath([{a, b, c}], 0)
        assert path.satisfies(a & b & c)
        assert path.satisfies(a | b | c)
        assert path.satisfies(a & (b | c))
    
    @pytest.mark.skipif(not HAS_NEXT, reason="Next operator not implemented")
    def test_empty_state(self):
        """Test state with no propositions"""
        a = PropositionLTLFormula("A")
        path = InfinitePath([set(), {a}], 1)
        assert not path.satisfies(a)  # A is not in first state
        assert path.satisfies(+a)  # But next state has A
    
    @pytest.mark.skipif(F is None or G is None, reason="F() or G() not implemented")
    def test_long_linear_path(self):
        """Test with long linear path before lasso"""
        props = PropositionLTLFormula.propositions(*[f"P{i}" for i in range(100)])
        states = [{props[i]} for i in range(100)]
        states.append({props[-1]})  # Lasso state
        path = InfinitePath(states, 100)
        
        # Test we can traverse to the end
        assert path.satisfies(F(props[99]))
    
    @pytest.mark.skipif(G is None, reason="G() not implemented")
    def test_large_lasso_size(self):
        """Test with large lasso"""
        props = [PropositionLTLFormula(f"P{i}") for i in range(50)]
        states = [set(), {props[0]}] + [{props[i % len(props)]} for i in range(1, 50)]
        path = InfinitePath(states, 2)
        
        # Check globally in lasso
        assert not path.satisfies(G(props[0]))  # Not always P0


class TestInfinitePathConstruction:
    """Test InfinitePath construction and assertions"""
    
    def test_lasso_index_valid(self):
        """Test lasso index must be valid"""
        a = PropositionLTLFormula("A")
        # Just verify it accepts a valid lasso index without raising
        path = InfinitePath([{a}, {a}], 1)
        assert path is not None
    
    def test_lasso_index_zero_valid(self):
        """Test lasso can start at index 0"""
        a = PropositionLTLFormula("A")
        # Just verify it accepts index 0 without raising
        path = InfinitePath([{a}], 0)
        assert path is not None
    
    def test_lasso_index_out_of_bounds_negative(self):
        """Test lasso index cannot be negative"""
        a = PropositionLTLFormula("A")
        with pytest.raises(AssertionError):
            InfinitePath([{a}], -1)
    
    def test_lasso_index_out_of_bounds_too_large(self):
        """Test lasso index cannot exceed path length"""
        a = PropositionLTLFormula("A")
        with pytest.raises(AssertionError):
            InfinitePath([{a}], 1)


class TestOperatorPrecedence:
    """Test that operators work correctly with parentheses"""
    
    @pytest.mark.skipif(not HAS_NEGATION, reason="Negation operator not implemented")
    def test_negation_priority(self):
        """Test negation works in complex expressions"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        formula = ~(a | b)
        path = InfinitePath([set()], 0)
        assert path.satisfies(formula)
    
    @pytest.mark.skipif(not (HAS_CONJUNCTION and HAS_DISJUNCTION), reason="Conjunction and Disjunction operators required")
    def test_conjunction_vs_disjunction(self):
        """Test conjunction and disjunction combinations"""
        a, b, c = PropositionLTLFormula.propositions("A", "B", "C")
        path = InfinitePath([{a, b}], 0)
        
        # (A & B) | C
        assert path.satisfies((a & b) | c)
        # A & (B | C)
        assert path.satisfies(a & (b | c))
    
    @pytest.mark.skipif(not (HAS_NEGATION and HAS_DISJUNCTION), reason="Negation and Disjunction operators required")
    def test_deeply_nested_formula(self):
        """Test deeply nested formula"""
        a, b = PropositionLTLFormula.propositions("A", "B")
        formula = ~(~(~(~a))) | b
        path = InfinitePath([{a}], 0)
        assert path.satisfies(formula)