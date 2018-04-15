#   Copyright (c) 2011-2015, Pieter Eendebak <pieter.eendebak@gmail.com>
#   Copyright (c) 2009, TNO Science & Industry
#
#   THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
#   IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
#   OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
#   IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
#   INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
#   NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
#   THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#   Complete Enumeration of Pure-Level and Mixed-Level Orthogonal Arrays, E.D.
#   Schoen, P.T. Eendebak, M.V.M. Nguyen, Volume 18, Issue 2, pages 123-140,
#   2010.
#   Two-Level Designs to Estimate All Main Effects and Two-Factor Interactions,
#   Pieter T. Eendebak, Eric D. Schoen, Technometrics Vol. 59 , Iss. 1, 2017
#
#   The code was written by:
#   Pieter Eendebak pieter.eendebak@gmail.com
#   Vincent Brouerius van Nidek
#   Alan Vazquez-Alcocer
#
#   Ideas contributed by:
#   Eric Schoen eric.schoen@tno.nl
#   Alan Vazquez-Alcocer alanrvazquez@gmail.com

import oapackage
import sys


def generate_orthogonal_array():
    """
    Example usage from:
    https://www.guru99.com/orthogonal-array-testing.html

    A Web page has three distinct sections (Top, Middle, Bottom) that can be
    individually shown or hidden from user

    No of Factors = 3 (Top, Middle, Bottom)
    No of Levels (Visibility) = 2 (Hidden or Shown)
    Array Type = L4(23)

    Test Cases 	TOP 	   Middle 	   Bottom
    Test #1 	Hidden 	   Hidden 	   Hidden
    Test #2 	Hidden 	   Visible 	   Visible
    Test #3 	Visible    Hidden 	   Visible
    Test #4 	Visible    Visible 	   Hidden

    Generate the test array (0-Hidden; 1-Visible)
    >> python orthogonalArray.py 2 4 3
    0   0   0
    0   1   1
    1   0   0
    1   1   1
    """

    # Levels (V) - Maximum number of values that can be taken on any single
    # factor.
    levels = int(sys.argv[1])   # Value range 0 till N
    # Runs (N) - Number of rows in the array, which translates into a number of
    # test cases that will be generated.
    runs = int(sys.argv[2])     # Rows
    # Factors (K) - Number of columns in the array, which translates into a
    # maximum number of variables that can be handled.
    factors = int(sys.argv[3])  # Columns

    print
    print('The Orthogonal array generated: L{}({}{})'.format(runs, levels, factors))
    print

    arrayclass = oapackage.arraydata_t(levels, runs, factors, factors)
    al = arrayclass.create_root()
    myarray = al.getarray()

    space = ' '
    for r in range(0, runs):
        row_data = ""
        for c in range(0, factors):
            val = myarray[r][c]
            row_data += '{}{}'.format(val, space*(4-len(str(val))))
        print(row_data)
    print


if __name__ == '__main__':
    try:
        generate_orthogonal_array()
    except Exception:
        print "python orthogonalArray.py [levels] [runs] [factors]"
