# -*- coding: utf-8 -*-

#   Copyright (c) 2015, MIT Probabilistic Computing Project
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""The Accounting Troll Model posits that all data values are equal to 9.

Reference: http://dilbert.com/strip/2001-10-25

This is an example of the simplest possible meta model.

This module implements the :class:`bayeslite.IBayesDBMetamodel`
interface for the Accounting Troll Model.
"""

import bayeslite.metamodel as metamodel

class TrollMetamodel(metamodel.IBayesDBMetamodel):
    """Accounting Troll metamodel for BayesDB.

    The metamodel is named ``accounting_troll`` in BQL::

        CREATE GENERATOR t_cc FOR t USING accounting_troll
    """

    def __init__(self): pass
    def name(self): return 'accounting_troll'
    def register(self, bdb):
        bdb.sql_execute("INSERT INTO bayesdb_metamodel (name, version) VALUES ('accounting_troll', 1)")
    def create_generator(self, bdb, table, schema, instantiate):
        instantiate(schema)
    def drop_generator(self, *args): pass
    def rename_column(self, *args): pass
    def initialize_models(self, *args): pass
    def drop_models(self, *args): pass
    def analyze_models(self, *args): pass
    def simulate_joint(self, _bdb, _generator_id, targets, _constraints):
        return [9 for _ in targets]
    def logpdf(self, _bdb, _generator_id, targets, constraints):
        for (_, _, value) in constraints:
            if not value == 9:
                return float("nan")
        for (_, _, value) in targets:
            if not value == 9:
                return float("-inf")
        # TODO This is only correct wrt counting measure.  What's the
        # base measure of numericals?
        return 0
    def insert(self, *args): pass
    def remove(self, *args): pass
    def infer(self, *args): pass
