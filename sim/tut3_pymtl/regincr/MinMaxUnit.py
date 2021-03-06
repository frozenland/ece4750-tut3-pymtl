#=========================================================================
# MinMax Unit
#=========================================================================
# This is a simple model for a Min/Max Unit.

from pymtl import *

class MinMaxUnit( Model ):

  # Constructor

  def __init__( s ):

    # Port-based interface

    s.in_ = InPort  ( Bits(8) )
    s.out = OutPort ( Bits(8) )

    # Concurrent block modeling register

    s.reg_out = Wire( Bits(8) )

    @s.tick
    def block1():
      if s.reset:
        s.reg_out.next = 0
      else:
        s.reg_out.next = s.in_
        
    @s.combinational
    def block2():
      s.out.value = s.reg_out + 1
      
  def line_trace(s):
    return "in:{} ({}) out:{}".format( s.in_, s.reg_out, s.out )


    # ''' TUTORIAL TASK '''''''''''''''''''''''''''''''''''''''''''''''''''
    # This model is incomplete. As part of the tutorial you will add a
    # combinational concurrent block to model the incrementer logic, and
    # later you will a line tracing function to compactly output the
    # input, register, and output vaules.
    # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

