import React, { useState, useEffect } from 'react';
import { Plus, Settings, AlignLeft, FileText, X, Save, Play } from 'lucide-react';

const PromptCardUI = () => {
  const [cards, setCards] = useState([
    {
      id: 1,
      title: 'Sales Analysis',
      description: 'Analyze sales data and suggest improvements',
      rules: [
        { type: 'instruction', content: 'Analyze the attached sales data from the perspective of a business analyst' },
        { type: 'format', content: 'Create a report with sections: Summary, Key Metrics, Areas for Improvement, and Action Items' },
        { type: 'constraint', content: 'Focus recommendations on top 3 highest impact areas only' }
      ],
      supportedFiles: ['csv', 'xlsx', 'pdf'],
      apiKey: 'claude-3-opus-20240229',
      files: [],
      expanded: false,
      editing: false
    },
    {
      id: 2,
      title: 'Code Refactoring',
      description: 'Refactor code for better performance',
      rules: [
        { type: 'instruction', content: 'Analyze the attached code for performance bottlenecks' },
        { type: 'format', content: 'Provide refactored code with comments explaining changes' },
        { type: 'constraint', content: 'Maintain the same functionality and API surface' }
      ],
      supportedFiles: ['js', 'ts', 'py', 'c', 'cpp'],
      apiKey: 'claude-3-opus-20240229',
      files: [],
      expanded: false,
      editing: false
    }
  ]);
  
  const [activeCard, setActiveCard] = useState(null);
  const [isCreatingCard, setIsCreatingCard] = useState(false);
  const [newCard, setNewCard] = useState({
    id: null,
    title: '',
    description: '',
    rules: [],
    supportedFiles: [],
    apiKey: 'claude-3-opus-20240229',
    files: [],
    expanded: true,
    editing: true
  });
  
  // Handle file drop
  const handleDrop = (e, cardId) => {
    e.preventDefault();
    
    // Update UI to show files have been added
    setCards(cards.map(card => {
      if (card.id === cardId) {
        // In a real app, we would process the actual files from e.dataTransfer.files
        return {
          ...card,
          files: [...Array(e.dataTransfer.files.length)].map((_, i) => ({
            name: `File ${i+1}`,
            type: 'document',
            size: '1.2 MB'
          }))
        };
      }
      return card;
    }));
  };
  
  // Handle drag over
  const handleDragOver = (e) => {
    e.preventDefault();
  };
  
  // Handle card execution
  const executeCard = (cardId) => {
    const card = cards.find(c => c.id === cardId);
    console.log(`Executing card: ${card.title}`);
    console.log(`Rules: ${card.rules.map(r => r.content).join(' | ')}`);
    console.log(`Files: ${card.files.map(f => f.name).join(', ')}`);
    console.log(`API: ${card.apiKey}`);
    
    // Here you would actually send the prompt and files to the AI API
    // and process the response
  };
  
  // Toggle card expanded state
  const toggleCardExpanded = (cardId) => {
    setCards(cards.map(card => {
      if (card.id === cardId) {
        return { ...card, expanded: !card.expanded };
      }
      return card;
    }));
  };
  
  // Create a new card
  const createNewCard = () => {
    setIsCreatingCard(true);
    setNewCard({
      ...newCard,
      id: cards.length + 1
    });
  };
  
  // Save new card
  const saveNewCard = () => {
    setCards([...cards, newCard]);
    setIsCreatingCard(false);
    setNewCard({
      id: null,
      title: '',
      description: '',
      rules: [],
      supportedFiles: [],
      apiKey: 'claude-3-opus-20240229',
      files: [],
      expanded: true,
      editing: true
    });
  };
  
  // Add a new rule to a card being edited
  const addRule = () => {
    setNewCard({
      ...newCard,
      rules: [...newCard.rules, { type: 'instruction', content: '' }]
    });
  };
  
  // Update a rule
  const updateRule = (index, field, value) => {
    const updatedRules = [...newCard.rules];
    updatedRules[index] = { ...updatedRules[index], [field]: value };
    setNewCard({ ...newCard, rules: updatedRules });
  };
  
  // Remove a file from a card
  const removeFile = (cardId, fileIndex) => {
    setCards(cards.map(card => {
      if (card.id === cardId) {
        const newFiles = [...card.files];
        newFiles.splice(fileIndex, 1);
        return { ...card, files: newFiles };
      }
      return card;
    }));
  };

  return (
    <div className="bg-gray-100 min-h-screen p-8">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-3xl font-bold mb-8">Prompt Card Dashboard</h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* Existing cards */}
          {cards.map(card => (
            <div 
              key={card.id}
              className="bg-white rounded-lg shadow-md overflow-hidden transition-all duration-200"
              style={{ height: card.expanded ? 'auto' : '180px' }}
            >
              <div className="p-5 border-b">
                <div className="flex justify-between items-center">
                  <h2 className="text-xl font-semibold">{card.title}</h2>
                  <div className="flex space-x-2">
                    <button 
                      onClick={() => toggleCardExpanded(card.id)}
                      className="p-1 rounded hover:bg-gray-100"
                    >
                      <AlignLeft size={16} />
                    </button>
                    <button className="p-1 rounded hover:bg-gray-100">
                      <Settings size={16} />
                    </button>
                  </div>
                </div>
                <p className="text-gray-600 mt-1">{card.description}</p>
              </div>
              
              {card.expanded && (
                <div className="p-5 border-b">
                  <h3 className="font-medium mb-2">Rules</h3>
                  <ul className="space-y-2">
                    {card.rules.map((rule, index) => (
                      <li key={index} className="flex items-start">
                        <span className="inline-block px-2 py-1 text-xs font-medium bg-blue-100 text-blue-800 rounded mr-2 mt-1">
                          {rule.type}
                        </span>
                        <span className="text-sm">{rule.content}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
              
              <div 
                className="p-5 border-b bg-gray-50"
                onDrop={(e) => handleDrop(e, card.id)}
                onDragOver={handleDragOver}
              >
                <div className="flex justify-between items-center mb-2">
                  <h3 className="font-medium">Files</h3>
                  <span className="text-xs text-gray-500">
                    Drag and drop files here
                  </span>
                </div>
                
                {card.files.length > 0 ? (
                  <ul className="space-y-2">
                    {card.files.map((file, index) => (
                      <li key={index} className="flex justify-between items-center bg-white p-2 rounded border">
                        <div className="flex items-center">
                          <FileText size={16} className="mr-2 text-gray-500" />
                          <span className="text-sm">{file.name}</span>
                        </div>
                        <button 
                          onClick={() => removeFile(card.id, index)}
                          className="text-gray-400 hover:text-red-500"
                        >
                          <X size={16} />
                        </button>
                      </li>
                    ))}
                  </ul>
                ) : (
                  <div className="border-2 border-dashed border-gray-300 rounded-lg p-4 text-center text-gray-400">
                    <p className="text-sm">No files added yet</p>
                  </div>
                )}
              </div>
              
              <div className="p-5 flex justify-end">
                <button 
                  onClick={() => executeCard(card.id)}
                  className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 flex items-center"
                  disabled={card.files.length === 0}
                >
                  <Play size={16} className="mr-2" />
                  Execute
                </button>
              </div>
            </div>
          ))}
          
          {/* Create new card button */}
          <div 
            className="border-2 border-dashed border-gray-300 rounded-lg flex items-center justify-center h-64 cursor-pointer hover:bg-gray-50"
            onClick={createNewCard}
          >
            <div className="text-center">
              <div className="w-12 h-12 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-2">
                <Plus size={24} className="text-gray-500" />
              </div>
              <p className="text-gray-500">Create New Prompt Card</p>
            </div>
          </div>
          
          {/* Card creation form (modal-like) */}
          {isCreatingCard && (
            <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
              <div className="bg-white rounded-lg w-full max-w-2xl">
                <div className="p-6 border-b">
                  <h2 className="text-xl font-semibold">Create New Prompt Card</h2>
                </div>
                
                <div className="p-6 space-y-4">
                  <div>
                    <label className="block text-sm font-medium mb-1">Card Title</label>
                    <input 
                      type="text" 
                      className="w-full p-2 border rounded" 
                      value={newCard.title}
                      onChange={(e) => setNewCard({...newCard, title: e.target.value})}
                      placeholder="e.g., Sales Analysis"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium mb-1">Description</label>
                    <input 
                      type="text" 
                      className="w-full p-2 border rounded" 
                      value={newCard.description}
                      onChange={(e) => setNewCard({...newCard, description: e.target.value})}
                      placeholder="Brief description of what this card does"
                    />
                  </div>
                  
                  <div>
                    <div className="flex justify-between items-center mb-2">
                      <label className="block text-sm font-medium">Rules</label>
                      <button 
                        className="text-sm text-blue-600 hover:text-blue-800"
                        onClick={addRule}
                      >
                        + Add Rule
                      </button>
                    </div>
                    
                    {newCard.rules.length > 0 ? (
                      <div className="space-y-3">
                        {newCard.rules.map((rule, index) => (
                          <div key={index} className="flex space-x-2">
                            <select 
                              className="p-2 border rounded"
                              value={rule.type}
                              onChange={(e) => updateRule(index, 'type', e.target.value)}
                            >
                              <option value="instruction">Instruction</option>
                              <option value="format">Format</option>
                              <option value="constraint">Constraint</option>
                            </select>
                            <input 
                              type="text" 
                              className="flex-1 p-2 border rounded"
                              value={rule.content}
                              onChange={(e) => updateRule(index, 'content', e.target.value)}
                              placeholder="Rule content..."
                            />
                          </div>
                        ))}
                      </div>
                    ) : (
                      <p className="text-sm text-gray-500">No rules added yet</p>
                    )}
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium mb-1">API Model</label>
                    <select 
                      className="w-full p-2 border rounded"
                      value={newCard.apiKey}
                      onChange={(e) => setNewCard({...newCard, apiKey: e.target.value})}
                    >
                      <option value="claude-3-opus-20240229">Claude 3 Opus</option>
                      <option value="claude-3-sonnet-20240229">Claude 3 Sonnet</option>
                      <option value="claude-3-haiku-20240307">Claude 3 Haiku</option>
                      <option value="gpt-4o">GPT-4o</option>
                    </select>
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium mb-1">Supported File Types</label>
                    <div className="flex flex-wrap gap-2">
                      {['csv', 'xlsx', 'pdf', 'txt', 'js', 'py', 'c', 'cpp'].map(type => (
                        <label key={type} className="flex items-center space-x-1 border rounded p-2">
                          <input 
                            type="checkbox"
                            checked={newCard.supportedFiles.includes(type)}
                            onChange={(e) => {
                              if (e.target.checked) {
                                setNewCard({...newCard, supportedFiles: [...newCard.supportedFiles, type]});
                              } else {
                                setNewCard({
                                  ...newCard, 
                                  supportedFiles: newCard.supportedFiles.filter(t => t !== type)
                                });
                              }
                            }}
                          />
                          <span className="text-sm">.{type}</span>
                        </label>
                      ))}
                    </div>
                  </div>
                </div>
                
                <div className="p-6 border-t bg-gray-50 flex justify-end space-x-3">
                  <button 
                    className="px-4 py-2 border rounded hover:bg-gray-100"
                    onClick={() => setIsCreatingCard(false)}
                  >
                    Cancel
                  </button>
                  <button 
                    className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 flex items-center"
                    onClick={saveNewCard}
                    disabled={!newCard.title}
                  >
                    <Save size={16} className="mr-2" />
                    Save Card
                  </button>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default PromptCardUI;