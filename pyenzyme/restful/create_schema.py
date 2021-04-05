# @Author: Jan Range
# @Date:   2021-03-19 15:03:19
# @Last Modified by:   Jan Range
# @Last Modified time: 2021-03-19 16:14:27

from marshmallow import fields, Schema

class EnzymeMLSchema(Schema):
    
    ############# General #################
    
    name = fields.Str(required=True)
    doi = fields.Str(required=False)
    pubmedID = fields.Str(required=False)
    url = fields.Str(required=False)
    
    ############# Creator #################

    class CreatorSchema(Schema):
        fname = fields.Str(required=True)
        gname = fields.Str(required=True)
        mail = fields.Str(required=True)
        
    creator = fields.List( fields.Nested(CreatorSchema()), required=True )

    ############# Vessels #################
    
    class VesselSchema(Schema):
        name = fields.Str(required=True)
        id_ = fields.Str(required=True)
        size = fields.Float(required=True)
        unit = fields.Str(required=True)
        
    vessel = fields.List( fields.Nested(VesselSchema), required=True)
    
    ############# Protein #################
    
    class ProteinSchema(Schema):
        name = fields.Str(required=True)
        sequence = fields.Str(required=True)
        compartment = fields.Str(required=True)
        init_conc = fields.Float(required=True)
        substanceunits = fields.Str(required=True)
        ecnumber = fields.Str(required=False)
        uniprotid = fields.Str(required=False)
        
    protein = fields.List( fields.Nested(ProteinSchema), required=True)
    
    ############# Reactants #################
    
    class ReactantSchema(Schema):
        name = fields.Str(required=True)
        compartment = fields.Str(required=True)
        init_conc = fields.Float(required=True)
        substanceunits = fields.Float(required=True)
        constant = fields.Boolean(required=True)
        smiles = fields.Str(required=False)
        inchi = fields.Str(required=False)
        
    reactant = fields.List( fields.Nested(ReactantSchema), required=True)
    
    ############# Reactions #################
    
    class ReactionSchema(Schema):
        name = fields.Str(required=True)
        temperature = fields.Float(required=True)
        tempunit = fields.Str(required=True)
        ph = fields.Float(required=True)
        reversible = fields.Boolean(required=True)
        
        class ElementSchema(Schema):
            species = fields.Str(required=True)
            stoich = fields.Float(required=True)
            constant = fields.Boolean(required=True)
            
            class ReplicateSchema(Schema):
                replica = fields.Str(required=True)
                reactant = fields.Str(required=True)
                type_ = fields.Str(required=True)
                data_unit = fields.Str(required=True)
                time_unit = fields.Str(required=True)
                init_conc = fields.Float(required=True)
                
                data = fields.List( fields.Float(required=True), required=True )
                time = fields.List( fields.Float(required=True), required=True )
            
            replicates = fields.List( fields.Nested(ReplicateSchema), required=True )
        
        educts = fields.List( fields.Nested(ElementSchema), required=True )
        products = fields.List( fields.Nested(ElementSchema), required=True )
        modifiers = fields.List( fields.Nested(ElementSchema), required=True )
        
        ############# Model #################
        
        class KineticModelSchema(Schema):
            equation = fields.Str(required=True)
            
            class ParameterSchema(Schema):
                name = fields.Str(required=True)
                reactant = fields.Str(required=True)
                value = fields.Float(required=True)
                unit = fields.Str(required=True)
            
            parameters = fields.List( fields.Nested(ParameterSchema), required=True )
            
        kineticmodel = fields.Nested(KineticModelSchema)
               
    reaction = fields.List( fields.Nested(ReactionSchema), required=True)
    
    