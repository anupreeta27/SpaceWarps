# ===========================================================================

import swap

# ======================================================================

class Crowd(object):
    """
    NAME
        Crowd

    PURPOSE
        Model a group of classifiers.

    COMMENTS
        The members of the Crowd are all Classifiers. The Crowd knows
        how big it is, and could, in principle, also know its mean
        expertise, and other qualities.

    INITIALISATION
        From scratch.
    
    METHODS
        Crowd.member(Name)     Returns the Classifier called Name
        Crowd.size()           Returns the size of the Crowd
        
    BUGS

    AUTHORS
      This file is part of the Space Warps project, and is distributed 
      under the GPL v2 by the Space Warps Science Team.
      http://spacewarps.org/

    HISTORY
      2013-04-17  Started Marshall (Oxford)
    """

# ----------------------------------------------------------------------------

    def __init__(self):
        self.name = 'Group of classifiers'
        self.member = {}
        return None

# ----------------------------------------------------------------------------

    def __str__(self):
        return 'Crowd of %d Classifiers' % (self.size())       
        
# ----------------------------------------------------------------------------

    def size(self):
        return len(self.member)
        
# ======================================================================
   