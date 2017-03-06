from system.memory import Memory
from system.manager import ProgramManager


class Processor(object):
    def __init__(self):
        self._mem = Memory()
        self.manager = ProgramManager()
        self.instructions = []
        self._carry = 0
        self._zero = 0

    @property
    def carry(self) -> int:
        return self._carry

    def set_carry(self, val: int):
        self._carry = val

    @property
    def zero(self) -> int:
        return self._zero

    def set_zero(self, val: int):
        self._zero = val

    @property
    def memory(self) -> Memory:
        return self._mem

    def execute(self) -> None:
        self.fetch_program(self.manager.pc).exec(self)

    def add_instruction(self, instr):
        self.instructions.append(instr)

    def fetch_program(self, addr: hex):
        return self.instructions[addr / Memory.PROGRAM_WIDTH]