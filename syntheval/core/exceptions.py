"""Domain exceptions."""
class SynthEvalError(Exception): pass
class InsufficientDataError(SynthEvalError): pass
